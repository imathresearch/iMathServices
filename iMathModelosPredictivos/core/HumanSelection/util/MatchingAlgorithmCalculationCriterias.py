'''
Created on 5 de oct. de 2015

@author: izubizarreta
'''

from iMathModelosPredictivos.core.HumanSelection.Works.Work import Work
from iMathModelosPredictivos.core.HumanSelection.Users.User import User

def getMatchingUserInterval(user, work, differenceAges):
    
    interval = [float(work.getEdad()) - differenceAges, float(work.getEdad()) + differenceAges]
    if float(user.getEdad()) == float(work.getEdad()):
        return 1
    else:
        if ((float(user.getEdad()) >= interval[0]) & (float(user.getEdad()) <= interval[1])):
            return 0.75
        else:
            return 0

def getMatchingUserHalfInterval(user, work, differenceAges):
    
    interval = [float(work.getEdad()) - (2 * differenceAges), float(work.getEdad()) + (2 * differenceAges)]
    if ((float(user.getEdad()) >= interval[0]) & (float(user.getEdad()) <= interval[1])):
        return 0.5
    else:
        return 0

def getJobMatching(user, work):
    
    AddValue = 0
    codeCross = 0
    
    for code in range(len(user.getJobs().getListOfJobs()) / 2):
        
        if float(user.getJobs().getListOfJobs()[codeCross]) == float(work.getJobs().getListOfJobs()[0]):
            AddValue = AddValue + 1
            if float(user.getJobs().getListOfJobs()[codeCross + 1]) >= float(work.getJobs().getListOfJobs()[1]):
                AddValue = AddValue + 1
            else:
                difference = float(user.getJobs().getListOfJobs()[codeCross + 1]) / float(work.getJobs().getListOfJobs()[1])
                AddValue = AddValue + difference
                
        codeCross = codeCross + 2
        
    return AddValue

def getDegreeMatching(user, work):
    
    AddValue = 0
    codeCross = 0
    
    for code in range(len(user.getDegrees().getListOfDegrees()) / 2):
        
        if float(user.getDegrees().getListOfDegrees()[codeCross]) == float(work.getDegrees().getListOfDegrees()[0]):
            AddValue = AddValue + 1
            if float(user.getDegrees().getListOfDegrees()[codeCross + 1]) == float(work.getDegrees().getListOfDegrees()[1]):
                AddValue = AddValue + 1
            else:
                difference = float(user.getDegrees().getListOfDegrees()[codeCross + 1]) / float(work.getDegrees().getListOfDegrees()[1])
                AddValue = AddValue + difference
                                
        codeCross = codeCross + 2
        
    return AddValue

def getLanguagesMatching(user, work):
    
    AddValue = 0
    codeCross = 0
    
    for code in range(len(user.getLanguages().getListOfLanguages()) / 2):
        
        if (float(user.getLanguages().getListOfLanguages()[codeCross]) == float(work.getLanguages().getListOfLanguages()[0])) & (float(user.getLanguages().getListOfLanguages()[codeCross]) > 0):
            AddValue = AddValue + 1
            if float(user.getLanguages().getListOfLanguages()[codeCross + 1]) == float(work.getLanguages().getListOfLanguages()[1]):
                AddValue = AddValue + 1
            else:
                difference = float(user.getLanguages().getListOfLanguages()[codeCross + 1]) / float(work.getLanguages().getListOfLanguages()[1])
                AddValue = AddValue + difference                
                
        codeCross = codeCross + 2
        
    return AddValue

def getTagsMatching(user, work):
    
    AddValue = 0
    codeCross = 0
    
    for code in user.getTags().getListOfTags():
        
        if (float(user.getTags().getListOfTags()[codeCross]) == float(work.getTags().getListOfTags()[0])) & (float(user.getTags().getListOfTags()[codeCross]) > 0):
            AddValue = AddValue + 1
            
        codeCross = codeCross + 1
        
    return AddValue
