'''
Created on 1 de oct. de 2015

@author: izubizarreta
'''
import random

class Languages(object):
    '''
    classdocs
    '''


    def __init__(self, ListOfLanguages, YearLanguages):
        '''
        Constructor
        '''
        self.ListOfLanguages = ListOfLanguages
        self.YearLanguages = YearLanguages

    def getListOfLanguages(self):
        
        MatrixFormat = []
        position = 0
        
        for language in self.ListOfLanguages:
            MatrixFormat.append(language)
            MatrixFormat.append(self.YearLanguages[position])
            position = position + 1
            
        return MatrixFormat
        
    def getLanguage(self, languagePosition):
        
        returnValue = [self.ListOfLanguages[languagePosition], self.YearLanguages[languagePosition]]
        return returnValue
        
    def setLanguage(self, newLanguage, years):
        
        self.ListOfLanguages.append(newLanguage)
        self.YearLanguages.append(years)
