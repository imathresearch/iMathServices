'''
Created on 5 de oct. de 2015

@author: izubizarreta
'''

import numpy as np
from iMathModelosPredictivos.core.src.Users.User import User
from iMathModelosPredictivos.core.src.Works.Work import Work
from iMathModelosPredictivos.core.src.util import MatchingAlgorithmCalculation as matchingCalculation
from iMathModelosPredictivos.core.src.util.ReadCriterias import Criterias
import iMathModelosPredictivos.core.src.util.RecoverCorrectUserWorkDatas as recoverData
#from MainPackage.MatchingAlgorithAndBestUserSelectionMainProgram import selectedUsers,

class CandidatesSelectedAlgorithm(object):
    '''
    classdocs
    '''


    def __init__(self, pathuser, pathWork, pathuseroriginal,pathworkoriginal,pathcriteria,number,priority):

        self.pathUser = pathuser
        self.pathWork = pathWork
        self.pathUserOriginal = pathuseroriginal
        self.pathWorkOriginal = pathworkoriginal
        self.pathCriteria = pathcriteria

        self.Users = np.genfromtxt(self.pathUser, dtype="|S50", delimiter=',', invalid_raise=False)
        self.WorkList = np.genfromtxt(self.pathWork, dtype="|S50", delimiter=',', invalid_raise=False)

        self.criteriaValues = Criterias(number,priority)
        
    def setStoreCandidatesWork(self):

        self.UserMatrix = []

        '''The following code recover the user's dat'''

        for user in self.Users:
      
            UserData = recoverData.getUserCriteriasValues(user)
        
            newUser = User(UserData[0], UserData[1], UserData[2], UserData[3], UserData[4], UserData[5], UserData[6], UserData[7], UserData[8])
    
            self.UserMatrix.append(newUser)
        
        '''The following code recover the work's data'''

        workData = recoverData.getWorkCriteriasValues(self.WorkList)
      
        self.newWork = Work(workData[0], workData[1], workData[2], workData[3], workData[4], workData[5], workData[6], workData[7], workData[8])
        
    def getSelectedUsers(self,number,priority):
   
        '''The following code calculates the matching value'''
    
        MatchingCalculationValues = matchingCalculation.generaMatchingAlgorithm(self.UserMatrix, self.newWork, self.criteriaValues.getMaximumDiffereneValue(), self.criteriaValues.getPercentageCriteriasValue())

        selectedUsers = matchingCalculation.selectBestNElements(MatchingCalculationValues, self.criteriaValues.getNumberOfElements(), self.UserMatrix)
        
        return selectedUsers

    def getCandidatesOriginalValues(self):

        UsersOriginal = np.genfromtxt(self.pathUserOriginal, dtype="|S50", delimiter=',', invalid_raise=False)
        
        return UsersOriginal
    
    def getNecessaryData(self,user,UsersOriginal):

        '''Visualization process'''

        positionUserOriginal = np.where(user.getId()==UsersOriginal[:,0])
        NameUser = UsersOriginal[positionUserOriginal,1]
        DireccionUser = UsersOriginal[positionUserOriginal,2]
        CodigoPostalUser = UsersOriginal[positionUserOriginal,3]
        ProvinciaUser = UsersOriginal[positionUserOriginal,4]
        TelephoneUser = UsersOriginal[positionUserOriginal,5]
        EmailUser = UsersOriginal[positionUserOriginal,6]
        cvsPath = 'Handlers/cvs/CV_' + str(positionUserOriginal[0][0]) + '.pdf'
        NecessaryData = [NameUser,DireccionUser,CodigoPostalUser,ProvinciaUser,TelephoneUser,EmailUser,cvsPath]
        return NecessaryData