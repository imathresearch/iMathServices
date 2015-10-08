'''
Created on 4 de oct. de 2015

@author: izubizarreta
'''

from iMathModelosPredictivos.core.HumanSelection.Users.User import User
from iMathModelosPredictivos.core.HumanSelection.Degrees.Degrees import Degrees
from iMathModelosPredictivos.core.HumanSelection.Jobs.Jobs import Jobs
from iMathModelosPredictivos.core.HumanSelection.Languages.Languages import Languages
from iMathModelosPredictivos.core.HumanSelection.Tags.Tags import Tags

def getMatrixUser(ClassMatrix):
         
    MatrixFormatData = []
    
    for row in ClassMatrix:
            
        rowMatrixData = []
        
        id = row.getId()
        edad = row.getEdad()
        jobs = row.getJobs()
        degrees = row.getDegrees()
        languages = row.getLanguages()
        tags = row.getTags()
            
        rowMatrixData.append(id)
        rowMatrixData.append(edad)
            
        for job in jobs.getListOfJobs():                
            rowMatrixData.append(job)
            
        for degree in degrees.getListOfDegrees():                
            rowMatrixData.append(degree)
                
        for language in languages.getListOfLanguages():                
            rowMatrixData.append(language)
                                     
        for tag in tags.getListOfTags():                
            rowMatrixData.append(tag)
            
        MatrixFormatData.append(rowMatrixData)
        
    return MatrixFormatData
