import sklearn
from sklearn.preprocessing.imputation import Imputer
from sklearn import preprocessing
from sklearn import svm
import numpy as np
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from sklearn.base import TransformerMixin
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import random
from sklearn.svm import SVC
from sklearn.feature_selection import RFECV

class DataFrameImputer(TransformerMixin):

    def __init__(self):
        """Impute missing values.

        Columns of dtype object are imputed with the most frequent value 
        in column.

        Columns of other types are imputed with mean of column.

        """
    def fit(self, X, y=None):

        self.fill = pd.Series([X[c].value_counts().index[0]
            if X[c].dtype == np.dtype('O') else X[c].mean() for c in X],
            index=X.columns)

        return self

    def transform(self, X, y=None):
        return X.fillna(self.fill)
 
def generateRandomValue():
    randomValue = random.random()
    return randomValue

def categoricalImputation(data, imputator=None):
    """Imputs categorical data
    Args:
        data (numpy 2-D array): array that contains the data with the missing values
        imputator (DataFrameImputer object): represents the object used to carry out a previously imputation
    Return:
        completeFrame.values (numpy 2-D array): array that contains the original data values plus the imputed ones
        imp (DataFrameImputer object): returned in the case that the imputator parameter is missing
    """
    if imputator != None:
        data = [[elem if elem != 'nan' else None for elem in row ]for row in data.tolist()]
        frame = pd.DataFrame(data)
        completeFrame = imputator.transform(frame);
        return completeFrame.values
    else:
        data = [[elem if elem != 'nan' else None for elem in row ]for row in data.tolist()]
        frame = pd.DataFrame(data)
        imp = DataFrameImputer();
        completeFrame = imp.fit_transform(frame)
        return [completeFrame.values, imp]
       

def numericalImputation(data, strategy=None, imputator=None):
    """Imputs numerical data
    Args:
        data (numpy 2-D array): array that contains the data with the missing values
        strategy (string): string that indicates the strategy to be used in the imputation ("mean", "median", "most_frequent")
        imputator (Imputer object): represents the object used to carry out a previously imputation
    Return:
        completeData (numpy 2-D array): array that contains the original data values plus the imputed ones
        imp (Imputer object): returned in the case that the imputator parameter is missing
    """
    if imputator != None:
        completeData = imputator.transform(data);
        return completeData
    elif strategy != None:
        imp = Imputer(missing_values='NaN', strategy=strategy, axis=0)
        completeData = imp.fit_transform(data);
        return [completeData, imp]
    else:
        print "ERROR"    

def maxminScaler(data, minInterval=0, maxInterval=1, scaler=None):
    """Scale the numerical data set to an interval specified by [minInterval, maxInterval]
    Args:
        data (numpy 2-D array): array that contains the data to be scaled
        minInterval (integer): represent the lower limit used to scale the data
        maxInterval (integer): represent the upper limit used to scale the data
        scaler (MinMaxScaler object): object previously trained to perform the scale process
    Returns:
        scaleData (numpy 2-D array): array of data to be scaled
        scaler (MinMaxScaler object): returned in the case that the scaler parameter is missing
    """
    if scaler != None:            
        scaleData = scaler.transform(data);
        return scaleData
    else:
        interval = (minInterval, maxInterval);
        scaler = preprocessing.MinMaxScaler(feature_range=interval)
        scaleData = scaler.fit_transform(data);
        return [scaleData, scaler]

def KFold(X, Y, classiferClass, **kwargs):
    """Evaluate the quality of the model
    Args:
        X (numpy array): contains the data set of input variables
        Y (numpy array): contains the target data model
        classiferClass (classifier object): classifier to be used to validate the model
        **kwargs: parameter used by the classifier
    Returns:
        Y_pred (numpy array): contains the predictions (belong or not belong)
    """        
    # Construct a kfolds object
    kf = sklearn.cross_validation.KFold(len(Y), n_folds=3, shuffle=True)
    Y_pred = Y.copy().ravel()
    # Iterate through folds
    for train_index, test_index in kf:            
        X_train, X_test = X[train_index], X[test_index]
        Y_train = Y[train_index]
        # Initialize a classifier with key word arguments
        clf = classiferClass(**kwargs)
        clf.fit(X_train, Y_train.ravel())
        Y_pred[test_index] = clf.predict(X_test)
   
    return Y_pred
    
def KFoldProb(X, Y, num_classes, classiferClass, **kwargs):
    """Evaluate the quality of the model
    Args:
        X (numpy array): contains the data set of input variables
        Y (numpy array): contains the target data model
        classiferClass (classifier object): classifier to be used to validate the model
        **kwargs: parameter used by the classifier
    Returns:
        Y_pred (numpy array): contains the predictions in form of probabilities
    """        
    kf = sklearn.cross_validation.KFold(len(Y), n_folds=5, shuffle=True)
    Y_prob = np.zeros((len(Y), num_classes))
    for train_index, test_index in kf:
        X_train, X_test = X[train_index], X[test_index]
        Y_train = Y[train_index]
        clf = classiferClass(**kwargs)
        clf.fit(X_train, Y_train.ravel())
        # Predict probabilities, not classes
        Y_prob[test_index] = clf.predict_proba(X_test)
        
    return Y_prob

def binarizer(XColumn, typeOf, onehotencoder=None, dic_variableList=None):
    """Wrap the functionality to binarise a variable
    Args:
        XColum (numpy array): array the represents the data of a SINGLE variable to be binarised
        typeOf (string): string that indicates the kind of binarisation method to be used
        onehotencoder (OneHotEncoder object): object previously created and trained to carry out a one hot encoder process
        dic_variableList (dictionary or list): contains all the values that the variable can have. It will be a dic for one hot encoder binarisation and a list for n hot encoder binarisation
    """
    if typeOf == '1HOT':
        return binarizerOneHotEnconding(XColumn, encoder=onehotencoder, dic=dic_variableList);
    elif typeOf == 'NHOT':
        return binarizerNHotEnconding(XColumn, variableList=dic_variableList)
    
def binarizerOneHotEnconding(XColumn, encoder=None, dic=None):
    """Perform one hot encoding binarisation over a SINGLE variable column data
       The transformation of categorical data to numerical labeled data carried out by "buildDictionary" and "mapCategoricalDictionary"
       is required to apply the method OneHotEncoder, which only works with numerical data
    Args:
        XColumn (numpy array): array the represents the column data of a SINGLE variable to be binarised
        encoder (OneHotEncoder object): object previously created and trained to carry out a one hot encoder process
        dic (dictionary): contains all the possibles values that the variables have, and the label number associated to this value 
                        dic['value'] = label_number
    Returns:
        dic (dictionary): contains all the possibles values that the variables have, and the label number associated to this value 
                        dic['value'] = label_number
        binarizerColumn (list): binarised variable 
    """
    if encoder != None:
        X = mapCategoricalDictionary(XColumn, dic);
        binarizerXColumn = encoder.transform(np.vstack(X)).toarray()
        return binarizerXColumn.tolist();       
    else:   
        dic = {}
        [dic, maxNumValues] = buildDictionary(XColumn);
        X = mapCategoricalDictionary(XColumn, dic);
        enc = OneHotEncoder(n_values=[maxNumValues])
        binarizerXColumn = enc.fit_transform(np.vstack(X)).toarray()
        return [dic, binarizerXColumn.tolist(), enc];
    

def binarizerNHotEnconding(XColumn, variableList=None):
    """Perform N hot encoding binarisation over a SINGLE variable column data
    Args:
        XColumn (numpy array): array the represents the column data of a SINGLE variable to be binarised
        variableList (list):contains all the possibles values that the variables have
    Returns:
        variableList (list): contains all the possibles values that the variables have
        binarizerColumn (list): binarised variable 
    """
    if variableList == None:
        variableList = list(set([elem for row in XColumn for elem in row.split(';') ]))
        binarizerXColumn = []
        for indexRow in range(len(XColumn)):
            row = XColumn[indexRow]
            binarizerXColumn = binarizerXColumn + binarizerNHotEncondingRow(row, variableList)
        return [variableList, binarizerXColumn]
    else:
        binarizerXColumn = []
        for indexRow in range(len(XColumn)):
            row = XColumn[indexRow]
            binarizerXColumn = binarizerXColumn + binarizerNHotEncondingRow(row, variableList)
        return binarizerXColumn
    
def binarizerNHotEncondingRow(XRow, variableList):
    """Perform N hot encoding binarisation over a SINGLE value
    Args:
        XRow (value): represents a specific value to be binarised
    Returns:
        binarizerRow (list): XRow binarised
    """ 
    binarizerRow = [0.0] * len(variableList)
    for elem in XRow.split(';'):
        if elem in variableList:
            binarizerRow[variableList.index(elem)] = 1.0;
        else:
            binarizerRow[variableList.index('unknown')] = 1.0;
    return [binarizerRow];  
    
def mapCategoricalDictionary(XColumn, dic):
    """Transform the categorical values of a data column SINGLE variable to its numerical "labeled" representation
    Args:
        XColumn (numpy array): array the represents the column data of a SINGLE variable to be transformed
        dic (dictionary): dictionary that contains for each value of XColumn it numerical labeled representation
    Returns:
        XColumn (numpy array): array transformed to labeled numerical data
    """
    for i in range(XColumn.shape[0]):
        if XColumn[i] in dic:
            XColumn[i] = dic[XColumn[i]]
        else:
            XColumn[i] = dic['unknown']
    return XColumn;
    
def buildDictionary(XColumn):
    """Given a data column SINGLE variable, build a dictionary that contains each value that the variable can have
       Each value has assigned a number as a label.
    Args:
        XColumn (numpy array): array the represents the column data of a SINGLE variable
    Returns:
        dic (dictionary): contains dic['value'] = number_used_as_label
        counter (integer): number of different values in XColumn
    """
    dic = {}
    counter = 0;
    for c in XColumn:
        if c not in dic:
            dic[c] = counter;
            counter = counter + 1;

    dic['unknown'] = counter;
    return [dic, counter + 1]

def svmOutliers (XData, thresh, classifier=None):
    """Calculate the outliers of XData set
    Args:
        XData (numpy array): contains the data where the detection of outliers is going to be carried out
        thresh (integer): indicates an approximation to the percent of outliers to be discovered in XData
        classifier (OneClassSVM object): object previously trained to perform detection of outliers
    Returns:
        index[0] (numpy array): contains the row index of the outliers in XData
        clf (OneClassSVM object): object trained to find outliers following the pattern of XData
    """
    nu = 0.95 * thresh + 0.5
    if classifier == None:
        clf = svm.OneClassSVM(kernel="rbf", nu=nu);
        clf.fit(XData)
        prediction = clf.predict(XData)
        index = np.where(prediction < 0)
        return [index[0], clf]
    else:
        prediction = classifier.predict(XData)
        index = np.where(prediction < 0)
        return index[0]
 
def numericalOutliers(XColumn, thresh=3.5):
    """Calculate the outliers of a SINGLE column numerical variable
    Args:
        XColumn (numpy array): array the represents the column data of a SINGLE variable
        thresh:
    Return:
        index (numpy array):  contains the row index of the outliers in XColumn
    """
    if len(XColumn.shape) == 1:
        XColumn = XColumn[:, None]
    median = np.median(XColumn, axis=0)
    diff = np.sum((XColumn - median) ** 2, axis=-1)
    diff = np.sqrt(diff)
    med_abs_deviation = np.median(diff)
    modified_z_score = 0.6745 * diff / med_abs_deviation

    outliers = modified_z_score > thresh
    index = np.where(outliers == True)
    return index


def categoricalOutliers(XColumn, percent):
    """Calculate the outliers of a SINGLE column categorical variable
    Args:
        XColumn (numpy array): array the represents the column data of a SINGLE variable
        thresh:
    Return:
        orderAVF (numpy array):  contains the row index of the outliers in XColumn
    """
      
    dic = {}
    dic['unique'], dic['counts'] = np.unique(XColumn, return_counts=True)
    
    AVF = [0] * XColumn.shape[0]
    for i in range(XColumn.shape[0]):        
        value = XColumn[i]    
        index = dic['unique'].tolist().index(value);
        AVF[i] = AVF[i] + dic['counts'][index];        
    
    # Get the index of the element in ascendent order
    # Here we must introduce another condition because if the AVF value is the same for all the points
    # ... we are returning anyway the corresponding percent
    orderAVF = np.argsort(AVF)
    numOutliers = int((percent / 100.0) * len(AVF))
    return orderAVF[0:numOutliers];

def PCAFeatureReduction(XData, pca=None):
    """Apply feature reduction
    Args:
        XData (numpy array): array that contains the data to be reducted
        pca (PCA object): object previously trained to reduce the number of variables following an specific transformation
    Returns:
        XData (numpy array): new array that contains the transformed data
        pca (PCA object): object trained to reduce the set of variables following the pattern in XData
    """
    if pca != None:
        XData = pca.transform(XData)
        return XData;
    else:
        pca = PCA(n_components='mle')
        XData = pca.fit_transform(XData)
        return[XData, pca];
    
def featureSelection(XData, YData=None, selector=None):
    
    if selector != None:
        XData = selector.transform(XData)
        return XData;
    else:     
        selector = SelectKBest(chi2, k=40)
        XData = selector.fit_transform(XData, YData)
        return[XData, selector];
    
       
    
