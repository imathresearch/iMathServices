'''
Created on Nov 23, 2015

@author: izubizarreta
'''

import tornado.ioloop
import tornado.web
from iMathModelosPredictivos.common.util.iMathServicesError import iMathServicesError
from iMathModelosPredictivos.controllers.modelGoCustomerController import ModelGoCustomerController


class ChurnCustomerHandler(tornado.web.RequestHandler):
    
    def getParameterValue(self, param):
        
        value = self.get_argument(param)
        return value
    
    def getParameterValues(self, param):
        
        values = self.get_arguments(param)
        return values
    
    def get(self):
        
        typeOperation = int(self.getParameterValue("operation"))
        modelController = ModelGoCustomerController()

        if typeOperation == 0:
            resultController=modelController.executeCreateModel()
        elif typeOperation == 1:
                resultController=modelController.executeTest()
        elif typeOperation == 2:
                resultController=modelController.executePrediction()
        else:
            msg = "Unexpected Error: ", "Passing an unexpected parameter value"
            raise iMathServicesError(msg)
        self.write(resultController)
    
    def post(self):
        pass
        

                

