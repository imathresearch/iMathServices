from model import Model
from iMathModelosPredictivos.common.util.ioOperations import IOOperations
from iMathModelosPredictivos.common.constants import CONS
from iMathModelosPredictivos.common.util.masMovilError import MasMovilError


from scipy import spatial
from operator import itemgetter
import pickle
import numpy as np
import ujson
import collections
import csv

CONS=CONS()

class ModelUpCrossSelling(Model):
    '''
    Extends:
        Class Model from iMathMasMovil.core.model   
    '''
    
    def __init__(self, dataFile, classifierType=None):
        super(ModelUpCrossSelling,self).__init__(dataFile, classifierType)
        
    def loadModel(self, dataFile):
        """Abstract method to be implemented in one of the subclasses
        Args:
          dataFile (string): The file where the model, previously created and saved, resides.        
        """
        io = IOOperations(); 
        fileDesc = io.openFile(dataFile, 'r+');
        self.toSave = pickle.load(fileDesc);
        self.bonds_matrix = self.toSave['bonds_matrix'];
        self.bonds_dic = self.toSave['bonds_dic']
        self.name = self.toSave['name'];
        io.closeFile(fileDesc);
        print "[iMathResearch] Modelo basado en " + self.name + " cargado"
    
    def saveModel(self, pathFile):        
        """Abstract method to be implemented in one of the subclasses
        Args:
          pathFile (string): String that indicates the complete path of the file where the created model is going to be saved.          
        """
        self.toSave = {};
        self.toSave['bonds_matrix'] = self.bonds_matrix;
        self.toSave['bonds_dic'] = self.bonds_dic
        self.toSave['name'] = self.name;
        io = IOOperations(); 
        print "[iMathResearch] Guardando modelo basado en " + self.name + " en el fichero " + pathFile
        file_model = io.openFile(pathFile, 'w+');
        pickle.dump(self.toSave, file_model);
        io.closeFile(file_model);  
        
    def createModel(self, dataFile, classifierType):
        """Abstract method to be implemented in one of the subclasses
        Args:
          dataFile (string): The file where the data to create the model resides.
          classifierType (string): String that indicates the type of classifierType to be used to create the model 
              We will probably offer several classifier to create the same model
        """ 
        #Open and read data
        io = IOOperations();    
        file_data = io.openFile(dataFile, 'r')
        self.list_sub_bonds = [l.rstrip() for l in file_data.readlines()]
        io.closeFile(file_data)
        
        self.classiferClass = classifierType
        if self.classiferClass == 'Amazon':
            print "[iMathResearch] Creando modelo para up y cross selling basado en 'Amazon collaborative filtering'"
            self._fit()
            self.name = "Amazon collaborative filtering"
        
        print "[iMathResearch] Modelo para up y cross selling creado"  
            

    def _fit(self):
        io = IOOperations();
        file_bonds = io.openFile(CONS.MODEL_UPCROSS_LIST_BONOS, 'r+')
        list_cod_bonds = [l.rstrip() for l in file_bonds.readlines()]
        io.closeFile(file_bonds)

        self.bonds_matrix = np.zeros((len(self.list_sub_bonds), len(list_cod_bonds)))

        bond_id = 0
        # bonds_dic is a dictionary which contains for each bond cod, its column index in bonds_matrix
        self.bonds_dic = {} 
        for bond in list_cod_bonds:
            self.bonds_dic[bond] = bond_id
            bond_id +=1

        sub_id = 0
        for sub in self.list_sub_bonds:
            bonds = sub.split('\t')[1:]
            for b in bonds:
                self.bonds_matrix[sub_id][self.bonds_dic[b]] = 1
            sub_id += 1
    
    def testModel(self,dataFile, outputFile):
        """Abstract method to be implemented in one of the subclasses
        Args:
          dataFile (string): The file where the data to be classified resides.
          outputFile (string): String that indicates the complete path of the file where the result of the testing is going to be saved. 
        """
        #Open and read data
        io = IOOperations()
        file_data = io.openFile(dataFile, 'r+')
        self.list_sub_bonds = [l.rstrip() for l in file_data.readlines()]
        
        print "[iMathResearch] Realizando la evaluación del modelo"
        recommendation = self._predict('test')
                
        self.__generateResultFile(outputFile, recommendation, 'test')
        print "[iMathResearch] Resultado del testing del modelo guardado en " + outputFile
        
    
    def predictModel(self, dataFile, outputFile):
        """Abstract method to be implemented in one of the subclasses
        Args:
          dataFile (string): The file where the data to be classified resides.
          outputFile (string): String that indicates the complete path of the file where the result of the testing is going to be saved. 
        """
        #Open and read data
        io = IOOperations()
        file_data = io.openFile(dataFile, 'r+')
        self.list_sub_bonds = [l.rstrip() for l in file_data.readlines()]
        
        print "[iMathResearch] Realizando la predicción"
        recommendation = self._predict('predict')
                
        self.__generateResultFile(outputFile, recommendation, 'predict')
        print "[iMathResearch] Prediccion generada por el modelo guardada en el fichero " + outputFile
        
        
    def _predict(self, mode):
                
        dic_sub_recommended = {}        
        for sub in self.list_sub_bonds:
            line = sub.split('\t')
            if len(line) < 2:
                raise MasMovilError("[iMathResearch] Cada fila en el fichero de entrada debe contener al menos dos columnas: ID_SUBSCRIPCION    CODIGO_BONO")
            
            id_sub = line[0]     # Id de la subscripcion
            # dic_sub_recommended is a dictionary firstly indexed by the subscription id
            # For each subscription, there are two dictionaries:
            #    - current, which contains a list of the bonds associate with the subscription
            #    - recommended, having as target bond the first one, it contains a list of the bonds recommended by the algoritm
            dic_sub_recommended[id_sub] = {}
            bonds = line[1:]
            dic_sub_recommended[id_sub]['current'] = bonds
            if mode == 'test':
                target_bonds = bonds[0:1]
            if mode == 'predict':
                target_bonds = bonds
            
            # 1. Getting the row in the data matrix model that also buy the bonds specified in target_bonds
            sub_buy_target_bond = np.where(self.bonds_matrix[:,self.bonds_dic[target_bonds[0]]] > 0)[0].tolist()
            for i in range (1, len(target_bonds)):
                aux = np.where(self.bonds_matrix[:,self.bonds_dic[target_bonds[i]]] > 0)[0].tolist()
                sub_buy_target_bond = set(sub_buy_target_bond).intersection(aux)
            
            # 2. Getting the bonds that also have been bought by subscriptions that bought the target bond
            list_bonds = []
            index_target_bonds = []
            for b in target_bonds:
                index_target_bonds.append(self.bonds_dic[b])
            for sub in sub_buy_target_bond:
                bonds_to_compare = np.where(self.bonds_matrix[sub,:] > 0)[0].tolist()
                for b in bonds_to_compare:
                    if b not in index_target_bonds:
                        list_bonds.append(b)
            
            # 3. Calculating the similarity between the target bonds and the list of candidate bonds in list_bonds
            set_bonds = set(list_bonds)
            dic_similarity = {}
            for bond_compare in set_bonds:
                column_bond = self.bonds_matrix[:, bond_compare]
                similarity = 0
                for target_bond in target_bonds:
                    column_target_bond = self.bonds_matrix[:, self.bonds_dic[target_bond]]                                      
                    similarity += 1 - spatial.distance.cosine(column_target_bond, column_bond)
                dic_similarity[bond_compare] = similarity / len(target_bonds)
            
            # 4. Creating a list of tuples where each tuple contains the real cod associated to a bond and the similarity with the target bond
            list_recommended = []
            for bond, similarity in dic_similarity.items():
                for cod_bond, index in self.bonds_dic.items():
                        if bond == index:
                            list_recommended.append((cod_bond,similarity))                   
                            break
            
            # 5. Sorting list_recommended by similarity and returning the 5 bonds more similar to the targer bond
            list_recomendados = sorted(list_recommended,key=itemgetter(1),reverse=True)
            if len(list_recomendados) < 5:        
                dic_sub_recommended[id_sub]['recommended'] = [i[0] for i in list_recomendados]
            else:
                dic_sub_recommended[id_sub]['recommended'] = [i[0] for i in list_recomendados[:5]]
            
        return dic_sub_recommended
        
    def __generateResultFile(self, outputFile, recommendations, mode):
        
        io = IOOperations()
        file_result = io.openFile(outputFile, 'w+')
        sep = '----------------------------------------------\n'
        total = len(recommendations)
        header1 = "TOTAL DE SUBSCRIPCIONES " + str(total) + "\n"  
        file_result.write(header1)
        file_result.write(sep)
        
        if mode == 'test':
            header2 = "TASA DE ACIERTOS DETALLADA \n"
            file_result.write(header2)
            
            header3 = ["% BONOS RECOMENDADOS ACERTADOS", "NUMERO DE SUBSCRIPCIONES"]
            row =  '\t'.join(header3) + '\n'
            file_result.write(row)
            statistics = self._getStatistics(recommendations)
            for stat in statistics:
                sample = []
                sample.append(str(stat))
                sample.append(str(statistics[stat]))
                row =  '\t'.join(sample) + '\n' 
                file_result.write(row)
            file_result.write(sep)
        
        header4 = "DETALLE DE PREDICCION PARA CADA SUBSCRIPCION\n"
        file_result.write(header4)
        header5 = ["ID_SUBSCRIPCION", "BONOS_ACTUALES" , "BONOS_RECOMENDADOS"]
        row =  '\t'.join(header5) + '\n' 
        file_result.write(row)
        
        for sub in recommendations:
            sample = []
            sample.append(str(sub))
            sample.append(ujson.dumps(map(int,recommendations[sub]['current'])))
            sample.append(ujson.dumps(map(int,recommendations[sub]['recommended'])))
            row =  '\t'.join(sample) + '\n'
            file_result.write(row)
          
        io.closeFile(file_result)
        
    def _getStatistics(self, recommendations):
        
        percent_hits = {}
        for sub in recommendations:
            hit = 0
            current = recommendations[sub]['current']
            recommended = recommendations[sub]['recommended']
            for i in range(1, len(current)):
                if current[i] in recommended:
                    hit = hit +1
            if len(current) == 1:
                percent = 100
            else:
                percent = round(int((float(hit) / (len(current)-1)) *100), -1)
            
            if percent in percent_hits:
                percent_hits[percent] = percent_hits[percent] + 1
            else:
                percent_hits[percent] = 1 
        
        return collections.OrderedDict(sorted(percent_hits.items(), reverse=True))