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
        
        return self.getColumnNames(table)
    
    def setStoreModel(self,table,parameters):
        
        self.ConnectionBBDD.setDataModel(table, parameters)
        
    def setStoreModelsResults(self,table,data):
        
        self.ConnectionBBDD.setDataModelResults(table, data)
       
    def closeConnection(self):
    
        self.ConnectionBBDD.closeConnection()