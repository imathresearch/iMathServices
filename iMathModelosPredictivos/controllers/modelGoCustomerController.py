from iMathModelosPredictivos.common.constants import CONS
from iMathModelosPredictivos.core.models.modelChurnCustomer import ModelChurnCustomer
from sklearn.ensemble import RandomForestClassifier

class ModelGoCustomerController(object):

    def __init__(self):

        self.model = ModelChurnCustomer()


    def executeCreateModel(self):
        #self.model.loadModel()
        self.model.createModel(RandomForestClassifier)
        self.model.saveModel()
        return dict(model='model ok')


    def executeTest(self):

        self.model.testModel()
        return dict(result='test ok')


    def executePrediction(self):


        prediction = self.model.predictModel()
        return dict(result=prediction)


