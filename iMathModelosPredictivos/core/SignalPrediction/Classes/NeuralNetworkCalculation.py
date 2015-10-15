'''
Created on 14 de oct. de 2015

@author: izubizarreta
'''
from iMathModelosPredictivos.core.SignalPrediction.util.CSV import CSVClass
from iMathModelosPredictivos.common.util.ConnectionBBDDMysql import ConnectionBBDD
from iMathModelosPredictivos.core.SignalPrediction.util.DatesTimes import DatesTimes
from iMathModelosPredictivos.core.SignalPrediction.Data.StringOperations import StringOperations
from iMathModelosPredictivos.core.modelPredictPosition import ModelPredictUserPosition
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from time import gmtime, strftime
import time
import numpy as np
import math

class NeuralNetworkCalculation(object):
    '''
    classdocs
    '''


    def getConnection(self):
        
        userConnection = ConnectionBBDD()
        self.userConnection = userConnection

    def getQuery(self, model, table, tipo):
        
        query = "select salon,dormitorio,bano,cocina,real_tag from " + table
        query = query + " where model_id = " + model + " and execution_type = " + tipo
        query = query + " order by id desc"
        return query
    
    def getQueryPredictData(self, model, table, tipo):
        
        query = "select salon,dormitorio,bano,cocina from " + table
        query = query + " where model_id = " + model + " and execution_type = " + tipo
        query = query + " order by id desc"
        return query

    def RecoverData(self, query):
        
        self.userConnection.userConnection.DoConnection()
        RecoverData = self.userConnection.userConnection.getResults(query, ['salon', 'dormitorio', 'bano', 'cocina', 'etiqueta'])
        self.csvDataTrainingTest = CSVClass(RecoverData)
        
    def RecoverDataPredict(self, query):
        
        self.userConnection.userConnection.DoConnection()
        RecoverData = self.userConnection.userConnection.getResults(query, ['salon', 'dormitorio', 'bano', 'cocina'])
        self.csvData = CSVClass(RecoverData)
    
    def _createModel(self, pathTraining, typeClassifier):
        
        self.notSupervisedModel = ModelPredictUserPosition(pathTraining, eval(typeClassifier))
        
    def _saveModel(self, datafile):
        
        self.notSupervisedModel.saveModel(datafile)
           
    def _testData(self, pathTest, outputFile):
        
        self.notSupervisedModel.testModel(pathTest, outputFile)
        
    def _predictData(self, pathPredict, outputFile):
        
        self.notSupervisedModel.predictModel(pathPredict, outputFile)