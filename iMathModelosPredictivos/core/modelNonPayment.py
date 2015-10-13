# (C) 2015 iMath Research S.L. - All rights reserved.

""" Implements the class ModelNonPayment, a sub class of the class Model

Authors:

@author iMath
"""
from model import Model
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
import csv
import numpy as np
from sklearn.metrics import confusion_matrix
#import matplotlib.pyplot as plt
import pickle

from iMathModelosPredictivos.common.util.ioOperations import IOOperations
from iMathModelosPredictivos.common.util.miningUtil import numericalImputation
from iMathModelosPredictivos.common.util.miningUtil import categoricalImputation
from iMathModelosPredictivos.common.util.miningUtil import maxminScaler
from iMathModelosPredictivos.common.util.miningUtil import binarizer
from iMathModelosPredictivos.common.util.miningUtil import numericalOutliers
from iMathModelosPredictivos.common.util.miningUtil import categoricalOutliers
from iMathModelosPredictivos.common.util.miningUtil import svmOutliers
from iMathModelosPredictivos.common.util.miningUtil import PCAFeatureReduction
from iMathModelosPredictivos.common.util.miningUtil import featureSelection
from iMathModelosPredictivos.common.util.iMathServicesError import MasMovilError
from iMathModelosPredictivos.common.constants import CONS

CONS=CONS()



class ModelNonPayment(Model):
    '''
    Extends:
        Class Model from iMathMasMovil.core.model   
    '''
     
    def __init__(self, dataFile, classifierType=None):
        super(ModelNonPayment,self).__init__(dataFile, classifierType)

    def loadModel(self, dataFile):
        """Abstract method to be implemented in one of the subclasses
        Args:
          dataFile (string): The file where the model, previously created and saved, resides.        
        """
        io = IOOperations(); 
        fileDesc = io.openFile(dataFile, 'r+');
        self.toSave = pickle.load(fileDesc);
        self.model = self.toSave['model'];
        self.name = self.toSave['name'];
        self.index = self.toSave['index']
        self.headerTestFormat = self.toSave['headerTestFormat']
        self.headerPredictFormat = self.toSave['headerPredictFormat'] 
        self.imputatorNumerical = self.toSave['imputatorNumerical'];
        self.imputatorCategorical = self.toSave['imputatorCategorical'];
        self.scaler = self.toSave['scaler'];
        self.binaryEncoder = self.toSave['binaryEncoder'];
        self.feature_selector = self.toSave['featureSelector'] 
        #self.svmOutliers = self.toSave['svmOutliers']; 
        #self.PCAReduction = self.toSave['PCAReduction'];
        self.columnMetaData = self.toSave['columnMetaData'];
        io.closeFile(fileDesc);
        print "[iMathResearch] Modelo basado en " + self.name + " cargado"
        
    
    def createModel(self, dataFile, classifierType):
        """Abstract method to be implemented in one of the subclasses
        Args:
          dataFile (string): The file where the data to create the model resides.
          classifierType (string): String that indicates the type of classifierType to be used to create the model 
              We will probably offer several classifier to create the same model
        """ 
        self._generateMetaData();
        #Open and read data
        io = IOOperations(); 
        fileDesc = io.openFile(dataFile, 'r+');
        [self.headerTrain, self.XData, self.YData] = io.readTrainDataModelFile(fileDesc);
        io.closeFile(fileDesc);
        try:        
            self.__checkTrainDataFormat();
        except MasMovilError as e:
            print "Data Error: " , e.value
            return;
        else:        
            #Preprocess data: clean and structure data and transform categorical data
            self.__preprocessTrainData();
            
            #Create the model
            self.classiferClass = classifierType
            if self.classiferClass == DecisionTreeClassifier:
                print "[iMathResearch] Creando modelo basado en Decision Trees"
                self._fit(); #for DT
                self.name = "DecisionTree"
            elif self.classiferClass == SVC:
                print "[iMathResearch] Creando modelo basado en SVC"
                self._fit(probability=True);
                self.name = "SVC"
            elif self.classiferClass == RandomForestClassifier:
                print "[iMathResearch] Creando modelo basado en Random Forest"
                self._fit(n_estimators=10) # for random forest
                self.name = "RandomForest"
            else:
                raise MasMovilError("Clasificador no valido");
              
            quality = self.accuracyPercentage();
            print "[iMathResearch] Modelo basado en " + self.name + " creado. Calidad igual a %.3f" % quality
            
    def saveModel(self, pathFile):        
        """Abstract method to be implemented in one of the subclasses
        Args:
          pathFile (string): String that indicates the complete path of the file where the created model is going to be saved.          
        """
        self.toSave = {};
        self.toSave['model'] = self.model;
        self.toSave['name'] = self.name;
        self.toSave['headerTestFormat'] = self.headerTestFormat
        self.toSave['headerPredictFormat'] = self.headerPredictFormat
        self.toSave['index'] = self.index 
        self.toSave['imputatorNumerical'] = self.imputatorNumerical
        self.toSave['imputatorCategorical'] = self.imputatorCategorical
        self.toSave['scaler'] = self.scaler;
        self.toSave['binaryEncoder'] = self.binaryEncoder;
        #self.toSave['svmOutliers'] = self.svmOutliers;
        #self.toSave['PCAReduction'] = self.PCAReduction;
        self.toSave['featureSelector'] = self.feature_selector
        self.toSave['columnMetaData'] = self.columnMetaData
        io = IOOperations(); 
        print "[iMathResearch] Guardando modelo basado en " + self.name + " en el fichero " + pathFile
        fileDesc = io.openFile(pathFile, 'w+');
        pickle.dump(self.toSave, fileDesc);
        io.closeFile(fileDesc);
    
    def predictModel(self, dataFile, outputFile):
        """Abstract method to be implemented in one of the subclasses
        Args:
          dataFile (string): The file where the data to be classified resides.
          outputFile (string): String that indicates the complete path of the file where the prediction is going to be saved. 
        """
        #Open and read data
        io = IOOperations(); 
        fileDesc = io.openFile(dataFile, 'r+');
        [self.headerPredict, self.XData] = io.readTestDataModelFile(fileDesc);
        try:        
            self.__checkPredictDataFormat();
        except MasMovilError as e:
            print "Data Error: " , e.value
            return;
        else:
            ID = self.XData[:,0]
            self.XData = np.delete(self.XData, 0, axis=1)
            #self.loadModel(CONS.MODEL_FILE_LOCATION);
            self._preprocessTestData();
            prediction = self._predict()
            prediction[prediction < 1 ] = 0
           
            predictionProb = self._predictProb()
            # Compute confusion matrix
            self.__generatePredictionFile(outputFile, ID, prediction, predictionProb)
            print "[iMathResearch] Prediccion generada por el modelo guardada en el fichero " + outputFile
    
    def testModel(self, dataFile, outputFile):
        """Abstract method to be implemented in one of the subclasses
        Args:
          dataFile (string): The file where the data to be classified resides.
          outputFile (string): String that indicates the complete path of the file where the prediction is going to be saved. 
        """
        #Open and read data
        io = IOOperations(); 
        fileDesc = io.openFile(dataFile, 'r+');
        [self.headerTest, self.XData] = io.readTestDataModelFile(fileDesc);
        try:        
            self.__checkTestDataFormat();
        except MasMovilError as e:
            print "Data Error: " , e.value
            return;
        else:
            self.YData = self.XData[:,-1]
            self.XData = np.delete(self.XData, -1, axis=1)
            #self.loadModel(CONS.MODEL_FILE_LOCATION);
            self._preprocessTestData();
            prediction = self._predict()
            prediction[prediction < 1 ] = 0
           
            self.YData = map(int,self.YData)
            predictionProb = self._predictProb()
            # Compute confusion matrix
            cm = confusion_matrix(self.YData, prediction)
            self.__generateTestFile(outputFile, self.YData, prediction, predictionProb, cm)
            print "[iMathResearch] Resultado del testing del modelo guardado en " + outputFile

            #Plot confusion matrix
            '''            
            plt.matshow(cm)
            plt.title('Confusion matrix')
            plt.colorbar()
            plt.ylabel('True label')
            plt.xlabel('Predicted label')
            plt.show()
            '''
    
    def __splitDataVariableType(self):
        """Divide the variable in two set depending on its type (numerical or categorical)
           The information about how to split the complete set is determined by self.index,
           which contains the index of numerical and categorical varianles respect to the complete data set
        Returns:
            numerical (numpy array): contains the values for the numerical variables
            categorical (numpy array): contains the values for the categorical variables  
        """
        numerical = self.XData[:, self.index['numerical']]
        categorical = self.XData[:, self.index['categorical']]
        return [numerical,categorical]
        
    def __joinDataVariables(self, numerical, categorical):        
        """Join two set of variables (numerical and categorical) in one complete set
           The union respects the initial order of these variables in the complete data set
        Args:
            numerical (numpy array): contains the values for the numerical variables
            categorical (numpy array): contains the values for the categorical variables 
        """   
        completeData = []
        columnNumerical = 0
        columnCategorical = 0
        categoricalIndex = 0
        for variable in self.columnMetaData:
            if variable['type'] == 'NUM':               
                completeData = completeData + [numerical[:, columnNumerical]]
                columnNumerical = columnNumerical +1;                
            else:                            
                varIndex = self.index['categorical'][categoricalIndex]
                binarySize = len(self.columnMetaData[varIndex]['values'])               
                completeData = completeData + [categorical[:,range(columnCategorical, columnCategorical + binarySize)]]
                columnCategorical = columnCategorical + binarySize;
                categoricalIndex = categoricalIndex +1;

        self.XData = np.column_stack((list for list in completeData))       
    
    def __checkTrainDataFormat(self):
        """Check that the input data format (respect to variables orders) matches the format established in the configuration file
        Return:
            raise an exception if the format of the input data is incorrect
        """ 
        if len(self.headerTrainFormat) == len(self.headerTrain):
            for index in range(len(self.headerTrainFormat)):
                if self.headerTrainFormat[index] != self.headerTrain[index]:
                    raise MasMovilError("Formato incorrecto en los datos de entrada");            
        else:
            raise MasMovilError("Formato incorrecto en los datos de entrada"); 
    
    def __checkTestDataFormat(self):
        """Check that the input data format (respect to variables orders) matches the format established in the configuration file
        Return:
            raise an exception if the format of the input data is incorrect
        """ 
        if len(self.headerTestFormat) == len(self.headerTest):
            for index in range(len(self.headerTestFormat)):
                if self.headerTestFormat[index] != self.headerTest[index]:                
                    raise MasMovilError("Formato incorrecto en los datos de entrada");          
        else:
            raise MasMovilError("Formato incorrecto en los datos de entrada");
    
    def __checkPredictDataFormat(self):
        """Check that the input data format (respect to variables orders) matches the format established in the configuration file
        Return:
            raise an exception if the format of the input data is incorrect
        """         
        if len(self.headerPredictFormat) == len(self.headerPredict):
            for index in range(len(self.headerPredictFormat)):
                if self.headerPredictFormat[index] != self.headerPredict[index]:                
                    raise MasMovilError("Formato incorrecto en los datos de entrada");          
        else:
            raise MasMovilError("Formato incorrecto en los datos de entrada");
    
    def __preprocessTrainData(self):
        """Structure and transform the data to be applied to a prediction model.
           These actions are applied generally in a separated manner to each type of variables (numerical and categorical)
           The structure and transformation actions must include:
           - Imputation
           - Filling of missing data
           - Outliers detection
           - Binarization for categorical variables
           - Feature reducction
        """

        # SPLIT VARIABLES
        [numericalData, categoricalData] = self.__splitDataVariableType();                
        
        # NUMERICAL PREPROCESSING        
        # 1. IMPUTATION
        [numericalData, self.imputatorNumerical] = numericalImputation(numericalData, strategy='mean')
        # 2. OUTLIERS 
        # The code below should be used to detect and eliminate numericalOutliers
        #[numericalData, categoricalData] = self._numericalOutlier(numericalData, categoricalData)
        # 3. NORMALIZATION    
        [numericalData, self.scaler] = maxminScaler(numericalData);
               
        # CATEGORICAL PREPROCESSING
        # 1. IMPUTATION
        [categoricalData, self.imputatorCategorical] = categoricalImputation(categoricalData)
        # 2. OUTLIERS
        # The code below should be used to detect and elimanate categoricalOutliers
        #[categoricalData, numericalData] = self._categoricalOutlier(categoricalData, numericalData)
        # 3. BINARIZATION    
        binarizerData = []
        for column in range(categoricalData.shape[1]):
            varIndex = self.index['categorical'][column]
            if self.columnMetaData[varIndex]['codification'] == '1HOT':
                [self.columnMetaData[varIndex]['values'], binarizerColumn, self.binaryEncoder] = binarizer(categoricalData[:, column], self.columnMetaData[varIndex]['codification'])
            else:
                [self.columnMetaData[varIndex]['values'], binarizerColumn] = binarizer(categoricalData[:, column], self.columnMetaData[varIndex]['codification'])
                
            binarizerData = binarizerData + [binarizerColumn]
        categoricalData = np.column_stack((list for list in binarizerData))

        # JOIN VARIABLES
        self.__joinDataVariables(numericalData, categoricalData);
        
        [self.XData, self.feature_selector] = featureSelection(self.XData, self.YData)
           
        # OUTLIERS FOR BOTH KIND OF VARIABLES 
        #[outliers, self.svmOutliers] = svmOutliers(self.XData, 0.2)        
        #self.XData = np.delete(self.XData, (outliers), axis=0)
        #self.YData = np.delete(self.YData, (outliers), axis=0)
        
        # REDUCTION OF VARIABLES
        #[self.XData, self.PCAReduction] = PCAFeatureReduction(self.XData)
       
    
    def _preprocessTestData(self):  
        
        # SPLIT VARIABLES
        [numericalData, categoricalData] = self.__splitDataVariableType();
        
        # NUMERICAL PREPROCESSING        
        # 1. IMPUTATION
        numericalData = numericalImputation(numericalData, strategy='mean', imputator=self.imputatorNumerical)
        # 2. OUTLIERS 
        # The code below should be used to detect and eliminate numericalOutliers
        #[numericalData, categoricalData] = self._numericalOutlier(numericalData, categoricalData)
        # 3. NORMALIZATION    
        numericalData = maxminScaler(numericalData, scaler=self.scaler);
               
        # CATEGORICAL PREPROCESSING
        # 1. IMPUTATION
        categoricalData = categoricalImputation(categoricalData, imputator=self.imputatorCategorical)
        # 2. OUTLIERS
        # The code below should be used to detect and elimanate categoricalOutliers
        #[categoricalData, numericalData] = self._categoricalOutlier(categoricalData, numericalData)
        # 3. BINARIZATION    
        binarizerData = []
        for column in range(categoricalData.shape[1]):
            varIndex = self.index['categorical'][column]
            if self.columnMetaData[varIndex]['codification'] == '1HOT':
                binarizerColumn = binarizer(categoricalData[:, column], self.columnMetaData[varIndex]['codification'], onehotencoder=self.binaryEncoder, dic_variableList=self.columnMetaData[varIndex]['values'] )
            else:
                binarizerColumn = binarizer(categoricalData[:, column], self.columnMetaData[varIndex]['codification'], dic_variableList=self.columnMetaData[varIndex]['values'])
                
            binarizerData = binarizerData + [binarizerColumn]            
        categoricalData = np.column_stack((list for list in binarizerData)) 

        # JOIN VARIABLES
        self.__joinDataVariables(numericalData, categoricalData);
                
        self.XData = featureSelection(self.XData, None, self.feature_selector)
        
        # OUTLIERS FOR BOTH KIND OF VARIABLES 
        #outliers= svmOutliers(self.XData, 0.2, self.svmOutliers)        
        #self.XData = np.delete(self.XData, (outliers), axis=0)
        #self.ID = np.delete(self.ID, (outliers), axis=0)
        
        # REDUCTION OF VARIABLES
        #self.XData = PCAFeatureReduction(self.XData, self.PCAReduction)
                     
    
    def _readMetaDataFile(self):
        """Read the file that contains the model's metadata
           The metadata describe:
            - how many variables are involved as well as the order of them
            - which variables must be considered as numerical
            - which variables must be considered as categorical
            - which categorical variables must be binarised using 1HOT method
            - which categorical variables must be binarised using NHOT method
        """
        lines = [line.strip() for line in open(CONS.MODEL_FILE_METADATA)]
        count = 0;
        while count < len(lines):
            if (lines[count] == '<variable train format>'):
                self.headerTrainFormat = lines[count+1].split(',');
                count +=2
            elif (lines[count] == '<variable test format>'):
                self.headerTestFormat = lines[count+1].split(',');
                count +=2
            elif (lines[count] == '<variable predict format>'):
                self.headerPredictFormat = lines[count+1].split(',');
                count +=2
            elif (lines[count] == '<numerical>'):
                self.numericalVariables = lines[count+1].split(',');
                count +=2
            elif (lines[count] == '<categorical>'):
                self.categoricalVariables = lines[count+1].split(',');
                count +=2
            elif (lines[count] == '<1Hot>'):
                self.oneHotVariables = lines[count+1].split(',');
                count +=2
            elif (lines[count] == '<NHot>'):
                self.NHotVariables = lines[count+1].split(',');
                count +=2
            else:
                count = count +1;
           
    def _generateMetaData(self):
        """Create a data structure that contains the metadata information for each variable in the model.
           This data structure will be used along the different model's functions.
        """
        self._readMetaDataFile();
        self.columnMetaData = []
        self.index = {}
        self.index['numerical'] = []
        self.index['categorical'] = []
        self.index['oneHot'] = []
        self.index['NHot'] = []
        for i in range (0, len(self.headerTrainFormat)-1):
            name = self.headerTrainFormat[i]
            dic = {}
            dic['name'] = name;
            if name in self.numericalVariables:
                self.index['numerical'].append(self.headerTrainFormat.index(name))
                dic['type'] = 'NUM'
            elif name in self.categoricalVariables:
                self.index['categorical'].append(self.headerTrainFormat.index(name))
                dic['type'] = 'CAT'
                if name in self.oneHotVariables:
                    self.index['oneHot'].append(self.headerTrainFormat.index(name));
                    dic['codification'] = '1HOT'
                elif name in self.NHotVariables:
                    self.index['NHot'].append(self.headerTrainFormat.index(name));
                    dic['codification'] = 'NHOT'
            
            self.columnMetaData.append(dic);
       
        
    def _numericalOutlier(self, numericalData, categoricalData):
        """Wrap the workflow necessary to obtain the outliers from numerical data subset
           1. For each numerical variable, its outliers are detected. 
           2. When an outlier is detected, the entire row, where the outlier resides, is deleted
           3. Also the same row is eliminated from the set of categorical data and the target data
        Args:
            numericalData (numpy array): contains the values for the numerical variables
            categoricalData (numpy array): contains the values for the categorical variables
        Returns:
            numericalData (numpy array): contains the values for the numerical variables after deleting the outliers tuples
            categoricalData (numpy array): ccontains the values for the categorical variables after deleting the numerical outliers tuples 
        """
        for column in range(numericalData.shape[1]):
            index = numericalOutliers(numericalData[:, column])
            numericalData = np.delete(numericalData, (index), axis=0)
            categoricalData = np.delete(categoricalData, (index), axis=0)
            self.YData = np.delete(self.YData, (index), axis=0)
        
        return [numericalData, categoricalData]
    
    def _categoricalOutlier(self, categoricalData, numericalData):
        """Wrap the workflow necessary to obtain the outliers from categorical data subset
           1. For each variable, its outliers are detected. 
           2. When an outlier is detected, the entire row, where the outlier resides, is deleted
           3. Also the same row is eliminated from the set of numerical data and the target data
        Args:
            categoricalData (numpy array): contains the values for the categorical variables
            numericalData (numpy array): contains the values for the numerical variables            
        Returns:
            categoricalData (numpy array): ccontains the values for the categorical variables after deleting the outliers tuples    
            numericalData (numpy array): contains the values for the numerical variables after deleting the categorical outliers tuples
        """
        for column in range(categoricalData.shape[1]):            
            index = categoricalOutliers(categoricalData[:, column],10)
            categoricalData = np.delete(categoricalData, (index), axis=0)
            numericalData = np.delete(numericalData, (index), axis=0)
            self.YData = np.delete(self.YData, (index), axis=0)
        
        return [categoricalData, numericalData]
    
    def __generateTestFile(self, outputFile, ID, prediction, predictionProb, mc=None):
        
        content = []
        header = ['Clase real', 'Clase predicha']
        for cls in self.model.classes_:
            header.append("Prob CL-" + str(cls))
        
        content.append(header)
        hit = 0
        for indexSample in range(len(ID)):
            sample = []
            sample.append(ID[indexSample])
            sample.append(prediction[indexSample])
            for numCls in range(len(self.model.classes_)):
                sample.append(predictionProb[indexSample][numCls])            
            content.append(sample)
            if int(ID[indexSample]) == prediction[indexSample]:
                hit = hit +1;
        
        with open(outputFile, "w+") as f:
            total = len(ID)
            f.write("TOTAL DE MUESTRAS A PREDECIR " + str(total) + ". ACIERTOS " + str(hit) + '\n')
            f.write('\n')
            if mc is not None:
                f.write('MATRIZ DE CONFUSION (Eje x -- Reales ( Pagos, impagos)--, Eje y -- Predichos (Pagos, impagos)--)\n')
                np.savetxt(f, mc,fmt='%10.0f');                
                f.write('\n')
            f.write ("PREDICCION DETALLADA \n")
            writer = csv.writer(f, lineterminator="\n")
            writer.writerows(content)
            
    def __generatePredictionFile(self, outputFile, ID, prediction, predictionProb):
        
        content = []
        header = ['ID Contrato', 'Clase Predicha']
        for cls in self.model.classes_:
            header.append("Prob CL-" + str(cls))
        
        content.append(header)
        hit = 0
        for indexSample in range(len(ID)):
            sample = []
            sample.append(ID[indexSample])
            sample.append(prediction[indexSample])
            for numCls in range(len(self.model.classes_)):
                sample.append(predictionProb[indexSample][numCls])            
            content.append(sample)
            if int(ID[indexSample]) == prediction[indexSample]:
                hit = hit +1;
        
        with open(outputFile, "w+") as f:
            f.write ("PREDICCION DETALLADA \n")
            writer = csv.writer(f, lineterminator="\n")
            writer.writerows(content)
           
        