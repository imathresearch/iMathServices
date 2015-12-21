'''
Created on 1 de oct. de 2015

@author: izubizarreta
'''
import random

class Degrees(object):
    '''
    classdocs
    '''


    def __init__(self, ListOfDegrees, YearLanguages):
        '''
        Constructor
        '''
        self.ListOfDegrees = ListOfDegrees
        self.YearLanguages = YearLanguages
        
    def getListOfDegrees(self):
        
        MatrixFormat = []
        position = 0
        
        for degrees in self.ListOfDegrees:
            MatrixFormat.append(degrees)
            MatrixFormat.append(self.YearLanguages[position])
            position = position + 1
            
        return MatrixFormat
        
    def getDegree(self, position):
        
        return [self.ListOfDegrees[position], self.YearLanguages[position]]
        
    def setDegree(self, newDegree, Years):
        
        self.ListOfDegrees.append(newDegree)
        self.YearLanguages.append(Years)
