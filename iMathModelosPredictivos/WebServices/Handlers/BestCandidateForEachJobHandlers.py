'''
Created on Nov 23, 2015

@author: izubizarreta
'''

import tornado.ioloop
import tornado.web

import numpy as np
from iMathModelosPredictivos.core.HumanSelection.Users.User import User
from iMathModelosPredictivos.core.HumanSelection.Works.Work import Work
from iMathModelosPredictivos.core.HumanSelection.util import MatchingAlgorithmCalculation as matchingCalculation
from iMathModelosPredictivos.core.HumanSelection.util.ReadCriterias import Criterias
import iMathModelosPredictivos.core.HumanSelection.util.RecoverCorrectUserWorkDatas as recoverData 

class BestCandidateForEachJobHandler(tornado.web.RequestHandler):
    
    def getParameterValue(self, param):
        
        value = self.get_argument(param)
        return value
    
    def getParameterValues(self, param):
        
        values = self.get_arguments(param)
        return values
    
    def get(self):
        
        pathUser = self.getParameterValue("pathUser")      
        pathWork = self.getParameterValue("pathWork")
        pathCriteria = self.getParameterValue("pathCriteria")
        SelectedCandidates = self.getBestCandidates(pathUser, pathWork, pathCriteria)
        
        '''It is necessary to store somewhere (CSV or BBDD)'''
        
    def post(self):
        
        pathUser = self.getParameterValue("pathUser")      
        pathWork = self.getParameterValue("pathWork")
        pathCriteria = self.getParameterValue("pathCriteria")
        SelectedCandidates = self.getBestCandidates(pathUser, pathWork, pathCriteria)
        
        '''It is necessary to store somewhere (CSV or BBDD)'''
        
    def getBestCandidates(self, pathUser, pathWork, pathCriteria):

        Users = np.genfromtxt(pathUser, dtype="|S50", delimiter=',', invalid_raise=False)
        WorkList = np.genfromtxt(pathWork, dtype="|S50", delimiter=',', invalid_raise=False)

        criteriaValues = Criterias(pathCriteria)

        UserMatrix = []

        '''The following code recover the user's dat'''

        for user in Users:
      
            UserData = recoverData.getUserCriteriasValues(user)
        
            newUser = User(UserData[0], UserData[1], UserData[2], UserData[3], UserData[4], UserData[5], UserData[6], UserData[7], UserData[8])
    
            UserMatrix.append(newUser)
        
        '''The following code recover the work's data'''

        workData = recoverData.getWorkCriteriasValues(WorkList)
      
        newWork = Work(workData[0], workData[1], workData[2], workData[3], workData[4], workData[5], workData[6], workData[7], workData[8])
   
        '''The following code calculates the matching value'''
    
        MatchingCalculationValues = matchingCalculation.generaMatchingAlgorithm(UserMatrix, newWork, criteriaValues.getMaximumDiffereneValue(), criteriaValues.getPercentageCriteriasValue())

        selectedUsers = matchingCalculation.selectBestNElements(MatchingCalculationValues, criteriaValues.getNumberOfElements(), UserMatrix)

        return selectedUsers
