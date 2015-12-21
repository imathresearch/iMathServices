'''
Created on 4 de oct. de 2015

@author: izubizarreta
'''
from  iMathModelosPredictivos.core.src.Works.Work import Work

class MatchingAlgorithm(object):
    '''
    classdocs
    '''
    

    def __init__(self, Users, Work, ListMatchingValues):
        '''
        Constructor
        '''
        self.ListOfUsers = Users
        self.work = Work
        self.ListOfMatchingValues = ListMatchingValues
    
    def getListOfUsers(self):
        
        return self.ListOfUsers
    
    def getWork(self):
        
        return self.work
    
    def getListOfMatchingValues(self):
        
        return self.ListOfMatchingValues
    
    def getListOfMatchingValue(self, position):
        
        return self.ListOfMatchingValues[0]
