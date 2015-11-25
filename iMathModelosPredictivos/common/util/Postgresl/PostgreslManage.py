'''
Created on Nov 23, 2015

@author: izubizarreta
'''

from ConnectionBBDDPostgresl import ConnectionBBDD

class PostgreslManage(object):
    '''
    classdocs
    '''
    
    def __init__(self, params):
        '''
        Constructor
        '''
        self.ConnectionBBDD = ConnectionBBDD(params)
        self.ConnectionBBDD.DoConnection()
        
    def getQueryListFormat(self, query):
         
        ListData = self.ConnectionBBDD.getResultsList(query)
        return ListData
        
    def getQueryMatrixFormat(self,query):
        
        MatrixData = self.ConnectionBBDD.getResults(query)
        return  MatrixData
    
    def getPrimaryKey(self, table):
        
        maxValue = self.ConnectionBBDD.getNextPrimaryKey(table)
        return maxValue
    
    def getColumnNames(self,table):
        
        return self.ConnectionBBDD.getColumnNames(table)
    
    def getTrainingHeaders(self,table):
        
        return self.ConnectionBBDD.getColumnTrain(table)
    
    def getTestHeaders(self,table):
        
        return self.ConnectionBBDD.getColumnTest(table)

    def getPredictionHeaders(self,table):
        
        return self.ConnectionBBDD.getColumnPredict(table)
    
    def setStoreModel(self,table,parameters, serviceValue):
        
        self.ConnectionBBDD.setDataModel(table, parameters, serviceValue)
        
    def getObjectValue(self, query):
        
        return self.ConnectionBBDD.getObjectData(query)
        
    def setStoreModelsResults(self,table,data, probabilities, codes):
        
        self.ConnectionBBDD.setDataModelResults(table, data, probabilities, codes)
       
    def closeConnection(self):
    
        self.ConnectionBBDD.closeConnection()