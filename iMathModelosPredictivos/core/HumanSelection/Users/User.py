'''
Created on 1 de oct. de 2015

@author: izubizarreta
'''
from iMathModelosPredictivos.core.HumanSelection.Degrees.Degrees import Degrees
from iMathModelosPredictivos.core.HumanSelection.Jobs.Jobs import Jobs
from iMathModelosPredictivos.core.HumanSelection.Languages.Languages import Languages
from iMathModelosPredictivos.core.HumanSelection.Tags.Tags import Tags
import random

class User(object):
    '''
    classdocs
    '''


    def __init__(self, id, Edad, JobsValues, YearsEachJob, DegreesValues, YearsDegrees, LanguagesValues, YearsEachLanguage, TagsValues):
                
        '''
        Constructor
        '''
        
        self.id = id
        self.edad = Edad
        self.degreeUsers = Degrees(DegreesValues, YearsDegrees)
        self.jobsUsers = Jobs(JobsValues, YearsEachJob)
        self.languagesUser = Languages(LanguagesValues, YearsEachLanguage)
        self.tagsUsers = Tags(TagsValues)
        
    def getId(self):
        
        return self.id
    
    def getEdad(self):
        
        return self.edad
    
    def getDegrees(self):
        
        return self.degreeUsers
    
    def getJobs(self):
        
        return self.jobsUsers
    
    def getLanguages(self):
        
        return self.languagesUser
    
    def getTags(self):
        
        return self.tagsUsers
    
