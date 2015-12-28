from iMathModelosPredictivos.core.models.modelBestCandidates import ModelBestCandidates

class ModelBestCandidatesController(object):

    def __init__(self):
        self.model = None


    def execute(self,job_id, selected_number, priority):


        self.model= ModelBestCandidates(job_id, selected_number, priority)
        return self.model.execute()


