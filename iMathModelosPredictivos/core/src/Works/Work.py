'''
Created on 1 de oct. de 2015

@author: izubizarreta
'''

from  iMathModelosPredictivos.core.src.Degrees.Degrees import Degrees
from  iMathModelosPredictivos.core.src.Jobs.Jobs import Jobs
from  iMathModelosPredictivos.core.src.Languages.Languages import Languages
from  iMathModelosPredictivos.core.src.Tags.Tags import Tags
import random

class Work(object):
    '''
    classdocs
    '''


    def __init__(self, id, Edad, DegreesValues, YearsDegrees, JobsValues, YearsEachJob, LanguagesValues, YearsEachLanguage, TagsValues):
                
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
