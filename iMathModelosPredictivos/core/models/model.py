# (C) 2015 iMath Research S.L. - All rights reserved.

""" The module that implements an abstract Model, which must be instantiated as 
UserCategory, etc...

Authors:

@author iMath
"""
import abc
import numpy as np
import pandas as pd
from iMathModelosPredictivos.common.util.miningUtil import KFold
from iMathModelosPredictivos.common.util.miningUtil import KFoldProb
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.svm import OneClassSVM
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestClassifier
import operator
from iMathModelosPredictivos.common.util.Postgresl.PostgreslManage import PostgreslManage
from iMathModelosPredictivos.common.util.serialization.Serialization import Serialization
    
class Model(object):
        
    def __init__(self, configurationPath, tableModel, tableData, columnName, service, classifierType=None):
        """
        Args:
          dataFile (string): The file where the data to create the model resides.
          classifierType (string): String that indicates the type of classifierType to be used to create the model 
              We will probably offer several classifier to create the same model
              If classifierType is equal to None it means the dataFile contains a model previously created.    
        """
        self.connection = PostgreslManage(configurationPath)
        self.serialization = Serialization()
        
        if classifierType != None:            
            self.createModel(tableModel, tableData, columnName, classifierType);
        else:
            self.loadModel(tableModel, service);
    
    @abc.abstractmethod 
    def loadModel(self, tableModel, service):
        """Abstract method to be implemented in one of the subclasses
        Args:
          dataFile (string): The file where the model, previously created and saved, resides.        
        """  
        
    @abc.abstractmethod 
    def createModel(self, tableModel, tableData, columnName, classifierType):
        """Abstract method to be implemented in one of the subclasses
        Args:
          dataFile (string): The file where the data to create the model resides.
          classifierType (string): String that indicates the type of classifierType to be used to create the model 
              We will probably offer several classifier to create the same model               
        """                
    
    @abc.abstractmethod
    def saveModel(self, tableModel):        
        """Abstract method to be implemented in one of the subclasses
        Args:
          pathFile (string): String that indicates the complete path of the file where the created model is going to be saved.          
        """                
    
    @abc.abstractmethod    
    def testModel(self, tableModel, tableData, columnName):
        """Abstract method to be implemented in one of the subclasses
        Args:
          dataFile (string): The file where the data to be classified resides.
          outputFile (string): String that indicates the complete path of the file where the prediction is going to be saved. 
        """
   
    @abc.abstractmethod    
    def predictModel(self, tableModel, tableData, columnName):
        """Abstract method to be implemented in one of the subclasses
        Args:
          dataFile (string): The file where the data to be classified resides.
          outputFile (string): String that indicates the complete path of the file where the prediction is going to be saved. 
        """

    def accuracyPercentage(self):
        YPred = KFold(self.XData, self.YData, self.classiferClass)
        t_f = self.YData[:, 0] == YPred
        return np.mean(self.YData[:, 0] == YPred)

    def _fit(self, **kwargs):
        self.model = self.classiferClass(**kwargs)
        self.model.fit(self.XData, self.YData.ravel())        
        # FOR SVM ONE CLASS
        # self.model.fit(self.XData)
                
    def _predict(self):
        prediction = self.model.predict(self.XData);
        return prediction;
        
    def _predictProb(self):
        prediction = self.model.predict_proba(self.XData);
        return prediction; 
             
        
