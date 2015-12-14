# (C) 2015 iMath Research S.L. - All rights reserved.

""" The module that implements an abstract Model, which must be instantiated as 
UserCategory, etc...

Authors:

@author iMath
"""
import abc
import numpy as np
from iMathModelosPredictivos.common.util.miningUtil import KFold


class Model(object):
    __metaclass__ = abc.ABCMeta


    
    @abc.abstractmethod 
    def loadModel(self):
        """Abstract method to be implemented in one of the subclasses
        Args:
          dataFile (string): The file where the model, previously created and saved, resides.        
        """  
        
    @abc.abstractmethod 
    def createModel(self, classifierType):
        """Abstract method to be implemented in one of the subclasses
        Args:
          dataFile (string): The file where the data to create the model resides.
          classifierType (string): String that indicates the type of classifierType to be used to create the model 
              We will probably offer several classifier to create the same model               
        """                
    
    @abc.abstractmethod
    def saveModel(self):
        """Abstract method to be implemented in one of the subclasses
        Args:
          pathFile (string): String that indicates the complete path of the file where the created model is going to be saved.          
        """                
    
    @abc.abstractmethod    
    def testModel(self):
        """Abstract method to be implemented in one of the subclasses
        Args:
          dataFile (string): The file where the data to be classified resides.
          outputFile (string): String that indicates the complete path of the file where the prediction is going to be saved. 
        """
   
    @abc.abstractmethod    
    def predictModel(self):
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
             
        
