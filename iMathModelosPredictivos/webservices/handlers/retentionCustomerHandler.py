

import tornado.ioloop
import tornado.web
from iMathModelosPredictivos.controllers.modelRetentionCustomerController import ModelRetentionCustomerController
from iMathModelosPredictivos.common.util.iMathServicesError import iMathServicesError

class RetentionCustomerHandler(tornado.web.RequestHandler):

    def getParameterValue(self, param):

        value = self.get_argument(param)
        return value

    def getParameterValues(self, param):

        values = self.get_arguments(param)
        return values



    def get(self):

        customer_id = int(self.getParameterValue("customer_id"))
        modelController = ModelRetentionCustomerController()


        resultController=modelController.executePrediction(customer_id)

        self.write(resultController)

    def post(self):
        typeOperation = int(self.getParameterValue("customer_id"))
        modelController = ModelRetentionCustomerController()

        try:
            resultController=modelController.executePrediction()
        except:
            msg = "Unexpected Error: ", "Passing an unexpected parameter value"
            raise iMathServicesError(msg)
        self.write(resultController)
