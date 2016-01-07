from iMathModelosPredictivos.common.constants import CONS
from iMathModelosPredictivos.core.models.modelRetentionCustomer import ModelRetentionCustomer


class ModelRetentionCustomerController(object):

    def __init__(self):

       self.model = ModelRetentionCustomer()




    def executePrediction(self,customer_id):


        prediction = self.model.make_recommendation(customer_id)
        return dict(result=prediction)


