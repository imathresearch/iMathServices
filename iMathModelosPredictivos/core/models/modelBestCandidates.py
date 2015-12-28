from iMathModelosPredictivos.core.src.MainPackage.CandidatesSelectedAlgorithm import CandidatesSelectedAlgorithm

class ModelBestCandidates(object):

    def __init__(self, job_id, number, priority):

        self.job_id = job_id
        self.number_workers = number
        self.priority = priority

    def execute(self):

        self._selectCSV_to_build_model()

        self.candidateSelectedAlgorithm = CandidatesSelectedAlgorithm(self.pathUser,
                                                                 self.pathWork,
                                                                 self.pathUserOriginal,
                                                                 self.pathWorkOriginal,
                                                                 self.pathCriteria,
                                                                 self.number_workers,
                                                                 self.priority)
        self.candidateSelectedAlgorithm.setStoreCandidatesWork()
        self.selectedCandidates = self.candidateSelectedAlgorithm.getSelectedUsers(self.number_workers,
                                                                                   self.priority)
        candidatesOriginalData = self.candidateSelectedAlgorithm.getCandidatesOriginalValues()
        return self._writeCandidatesDataOnScreen(self.candidateSelectedAlgorithm,
                                                 self.selectedCandidates,
                                                 candidatesOriginalData)



    def _writeCandidatesDataOnScreen(self,candidateSelectedAlgorithm,selectedCandidates,candidatesOriginalData):


        bestCandidates = []
        for user in selectedCandidates:

            candidatesData = candidateSelectedAlgorithm.getNecessaryData(user,candidatesOriginalData)

            print candidatesData[0][0][0]
            print candidatesData[4][0][0]
            print candidatesData[5][0][0]
            print candidatesData[6]
            bestCandidates.append(dict(name=candidatesData[0][0][0],
                                       telephone=candidatesData[4][0][0],
                                       email=candidatesData[5][0][0],
                                       path_cv=candidatesData[6]))
        return bestCandidates

    def _selectCSV_to_build_model(self):

        self.pathUser = '../data/RRHH/resultsandidatesCodes'+self.job_id+'.csv'
        self.pathWork = '../data/RRHH/resultsWorkCodes'+self.job_id+'.csv'
        self.pathUserOriginal = '../data/RRHH/resultsCandidateOriginal'+self.job_id+'.csv'
        self.pathWorkOriginal = '../data/RRHH/resultsWorkOriginal'+self.job_id+'.csv'
        self.pathCriteria = '../data/RRHH/Criterias.txt'



