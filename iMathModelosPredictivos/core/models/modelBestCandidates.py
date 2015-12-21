from iMathModelosPredictivos.core.src.MainPackage.CandidatesSelectedAlgorithm import CandidatesSelectedAlgorithm

class ModelBestCandidates(object):

    def execute(self, number, priority):
        pathUser = '../data/RRHH/resultsandidatesCodes.csv'
        pathWork = '../data/RRHH/resultsWorkCodes.csv'
        pathUserOriginal = '../data/RRHH/resultsCandidateOriginal.csv'
        pathWorkOriginal = '../data/RRHH/resultsWorkOriginal.csv'
        pathCriteria = '../data/RRHH/Criterias.txt'
        candidateSelectedAlgorithm = CandidatesSelectedAlgorithm(pathUser,pathWork,pathUserOriginal,pathWorkOriginal,pathCriteria,number,priority)
        candidateSelectedAlgorithm.setStoreCandidatesWork()
        selectedCandidates = candidateSelectedAlgorithm.getSelectedUsers(number,priority)
        candidatesOriginalData = candidateSelectedAlgorithm.getCandidatesOriginalValues()
        return self.writeCandidatesDataOnScreen(candidateSelectedAlgorithm, selectedCandidates, candidatesOriginalData)

        #return dict(number=number, priority=priority)

    def writeCandidatesDataOnScreen(self,candidateSelectedAlgorithm,selectedCandidates,candidatesOriginalData):


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




