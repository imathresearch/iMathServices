'''
Created on 1 de oct. de 2015

@author: izubizarreta
'''

import random

class Jobs(object):
    '''
    classdocs
    '''


    def __init__(self, ListOfJobs, YearEachJob):
        '''
        Constructor
        '''
        self.ListOfJobs = ListOfJobs
        self.YearEachJob = YearEachJob
        
    def getListOfJobs(self):
        
        MatrixFormat = []
        position = 0
        
        for jobs in self.ListOfJobs:
            MatrixFormat.append(jobs)
            MatrixFormat.append(self.YearEachJob[position])
            position = position + 1
            
        return MatrixFormat
        
    def getJob(self, position):
        
        return [self.ListOfJobs[position], self.YearEachJob[position]]
        
    def setJob(self, newJob, YearEachJob):
        
        self.ListOfJobs.append(newJob)
        self.YearEachJob(YearEachJob)
