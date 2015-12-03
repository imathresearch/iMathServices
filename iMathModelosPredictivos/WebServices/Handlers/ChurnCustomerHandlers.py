'''
Created on Nov 23, 2015

@author: izubizarreta
'''

import tornado.ioloop
import tornado.web

import os

from iMathModelosPredictivos.core.models.modelGoCustomer import ModelGoCustomer
from iMathModelosPredictivos.common.constants import CONS
from iMathModelosPredictivos.common.util.iMathServicesError import iMathServicesError
from iMathModelosPredictivos.scripts_Baja.help import showExtendedHelp
from iMathModelosPredictivos.scripts_Baja.help import showShortHelp

from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

class ChurnCustomerHandler(tornado.web.RequestHandler):
    
    def getParameterValue(self, param):
        
        value = self.get_argument(param)
        return value
    
    def getParameterValues(self, param):
        
        values = self.get_arguments(param)
        return values
    
    def get(self):
        
        typeOperation = int(self.getParameterValue("operation"))
        self.executeFunction(typeOperation)
    
    def post(self):
        
        typeOperation = int(self.getParameterValue("operation"))
        self.executeFunction(typeOperation)
                
    def executeFunction(self, typeOperation):

        pathPostgresql ="/home/antonio/proyectos/iMathServices/iMathModelosPredictivos/data/ConfigurationValues/ConfigurationValuesPostgresql.txt"
        pathElasticSearch = "/home/antonio/proyectos/iMathServices/iMathModelosPredictivos/data/ConfigurationValues/ConfigurationValuesElasticsearch.txt"
        tableModel = "Model"
        tableData = "CompleteData"
        service = "ChurnCustomer"
        tableResults = "resultsModel"
        columnFilterData = "operationData"
        dictionaryName = "telcoresults"        
        if typeOperation == 0:
            self.executeCreateModel(pathPostgresql,pathElasticSearch,tableModel,tableData,columnFilterData,service,RandomForestClassifier)
        else:
            if typeOperation == 1:
                self.executeTest(pathPostgresql,pathElasticSearch,tableModel,tableData,columnFilterData,service,tableResults)
            else:
                self.executePrediction(pathPostgresql,pathElasticSearch,tableModel,tableData,columnFilterData,service,tableResults,dictionaryName)
        
    def executeCreateModel(self, pathPostgresql,pathElasticSearch, tableModel, tableData, columnName, service, classifierType):
        
        model = ModelGoCustomer(pathPostgresql,pathElasticSearch,tableModel,tableData,columnName,service,classifierType)
        self.write("Model created<br>")
        model.saveModel(tableModel, service)
        self.write("Model stored")
        
        #It is necessary to send an advise that the model is created and store.
        
    def executeTest(self, pathPostgresql,pathElasticSearch, tableModel, tableData, columnName, service,tableResults):
        
        model = ModelGoCustomer(pathPostgresql,pathElasticSearch,tableModel,tableData,columnName,service)
        self.write("Model loaded<br>")
        model.testModel(tableResults, tableData, columnName)
        self.write("Model tested<br>")
        
        #It is necessary to send an advise that the test process is finished.
                                
    def executePrediction(self, pathPostgresql,pathElasticSearch, tableModel, tableData, columnName, service,tableResults,dictionary):
        
        model = ModelGoCustomer(pathPostgresql,pathElasticSearch,tableModel,tableData,columnName,service)
        print "Model loaded<br>"
        prediction = model.predictModel(tableResults, tableData, columnName, dictionary)
        print "Prediction is done<br>"
        self.write({"result":prediction})
        
        #It is necessary to send an advise that the prediction is done.