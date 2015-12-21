from iMathModelosPredictivos.core.models.modelBestCandidates import ModelBestCandidates

class ModelBestCandidatesController(object):

    def __init__(self):
        pass
        self.model = ModelBestCandidates()


    def execute(self,selected_number, priority):


        return self.model.execute(selected_number, priority)


