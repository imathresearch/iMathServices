'''
Created on Nov 23, 2015

@author: izubizarreta
'''

import tornado.ioloop
import tornado.web

import os

from iMathModelosPredictivos.core.modelGoCustomer import ModelGoCustomer
from iMathModelosPredictivos.common.constants import CONS
from iMathModelosPredictivos.common.util.iMathServicesError import iMathServicesError
from iMathModelosPredictivos.scripts_Baja.help import showExtendedHelp
from iMathModelosPredictivos.scripts_Baja.help import showShortHelp

from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

class ChurnCustomerHandler(tornado.web.RequestHandler):
    
    def getParameterValue(self,param):
        
        value = self.get_argument(param)
        return value
    
    def getParameterValues(self,param):
        
        values = self.get_arguments(param)
        return values
    
    def get(self):
        
        typeOperation = self.getParameterValue("operation")
        self.executeFunction(typeOperation)
    
    def post(self):
        
        typeOperation = self.getParameterValue("operation")
        self.executeFunction(typeOperation)
                
    def executeFunction(self,typeOperation):
        
        if typeOperation == 0:
            pathCSV = self.getParameterValue("pathCSV")
            typeModel = self.getParameterValue("typeModel")
            nameModel = self.getParameterValue("nameModel")
            self.executeCreateModel(pathCSV, typeModel, nameModel)
        else:
            if typeOperation == 1:
                pathCSV = self.getParameterValue("pathCSV")
                nameModel = self.getParameterValue("nameModel")
                pathOutputFile = self.getParameterValue("pathOutputFile")
                self.executeTest(pathCSV, nameModel, pathOutputFile)
            else:
                pathCSV = self.getParameterValue("pathCSV")
                nameModel = self.getParameterValue("nameModel")
                pathOutputFile = self.getParameterValue("pathOutputFile")
                self.executePrediction(pathCSV, nameModel, pathOutputFile)
        
    def executeCreateModel(self,pathCSV,typeModel,nameModel):
        
        if os.path.isfile(pathCSV) is False:
            raise iMathServicesError("El fichero " + pathCSV + " no existe");
    
        # Check if the classifier exists
        if typeModel == 'DecisionTreeClassifier':
            classifier = DecisionTreeClassifier
        elif typeModel == "SVC":
            classifier = SVC
        elif typeModel == "RandomForestClassifier":
            classifier = RandomForestClassifier
        else:
            raise iMathServicesError("El clasificador " + typeModel + " no es valido")
        
        model = ModelGoCustomer(pathCSV, classifier);
        model.saveModel(CONS.MODEL_FILE_LOCATION + nameModel + '.txt');
        
    def executeTest(self,pathCSVInput,NameModel,OutputFile):
        
        # Check if the data file exists
        if os.path.isfile(pathCSVInput) is False:
            raise iMathServicesError("El fichero " + pathCSVInput + " no existe");
    
        # Check if the file that contains the model exists
        model_path = os.path.join(CONS.MODEL_FILE_LOCATION +  NameModel + ".txt")
        if os.path.isfile(model_path) is False:
            raise iMathServicesError("EL modelo " +   NameModel  + " no ha sido previamente creado");
    
        model = ModelGoCustomer(model_path);
        model.testModel(pathCSVInput, OutputFile);
        
    def executePrediction(self,pathCSVInput,NameModel,OutputFile):
        
        # Check if the data file exists
        if os.path.isfile(pathCSVInput) is False:
            raise iMathServicesError("El fichero " + pathCSVInput + " no existe");
    
        # Check if the file that contains the model exists
        model_path = os.path.join(CONS.MODEL_FILE_LOCATION +  NameModel + ".txt")
        if os.path.isfile(model_path) is False:
            raise iMathServicesError("EL modelo " +   NameModel  + " no ha sido previamente creado");
    
        model = ModelGoCustomer(model_path);
        model.predictModel(pathCSVInput, OutputFile);