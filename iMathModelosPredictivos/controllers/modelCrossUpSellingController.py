from iMathModelosPredictivos.common.constants import CONS
from iMathModelosPredictivos.core.models.modelUpCrossSelling import ModelUpCrossSelling


class ModelCrossUpSellingController(object):

    def __init__(self):

       self.model = ModelUpCrossSelling('Amazon')


    def executeCreateModel(self):
        #self.model.loadModel()
        self.model.createModel('Amazon')
        self.model.saveModel()
        return dict(model='model ok')


    def executeTest(self):

        self.model.testModel()
        return dict(result='test ok')


    def executePrediction(self):


        prediction = self.model.predictModel()
        return dict(result=prediction)


