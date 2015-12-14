from iMathModelosPredictivos.common.constants import CONS
from iMathModelosPredictivos.core.models.modelGoCustomer import ModelGoCustomer
from sklearn.ensemble import RandomForestClassifier

class ModelGoCustomerController(object):

    def __init__(self):

        self.model = ModelGoCustomer()


    def executeCreateModel(self):

        self.model.createModel(RandomForestClassifier)
        self.model.saveModel()
        return dict(model='model ok')


    def executeTest(self):

        self.model.testModel()
        return dict(result='test ok')


    def executePrediction(self):


        prediction = self.model.predictModel()
        return dict(result=prediction)


