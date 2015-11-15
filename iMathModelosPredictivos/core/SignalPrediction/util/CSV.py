'''
Created on 2 de oct. de 2015

@author: izubizarreta
'''

import numpy as np

class CSVClass(object):
    '''
    classdocs
    '''


    def __init__(self, path):
        '''
        Constructor
        '''
        
        '''Probably, the following code it will be necessary to modify.'''
        
        self.data = np.genfromtxt(path, dtype="|S50", delimiter=',', invalid_raise=False)
        self.header = self.data[0, :]
        self.X = self.data[1:, :-1]        
        self.Y = self.data[1:, -1:]      
        
    def getData(self):
        
        return self.data
    
    def getHeaders(self):
        
        return self.header
    
    def getVariables(self):
        
        return self.X
    
    def getLabels(self):
        
        return self.Y
