'''
Created on Nov 23, 2015

@author: izubizarreta
'''

from ConnectionBBDDPostgresl import ConnectionBBDD

class PostgreslManage(object):
    '''
    classdocs
    '''
    
    def __init__(self, host, user, password, database):
        '''
        Constructor
        '''
        self.ConnectionBBDD = ConnectionBBDD(host,
                                             user,
                                             password,
                                             database)

        
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
        
        return self.ConnectionBBDD.setDataModel(table, parameters, serviceValue)
        
    def getObjectValue(self, query):
        
        return self.ConnectionBBDD.getObjectData(query)
    
    def getCode(self, query):
        
        return self.ConnectionBBDD.getCode(query)
        
    def setStoreModelsResults(self,operation,table,data, probabilities, codes):
        
        self.ConnectionBBDD.setDataModelResults(operation, table, data, probabilities, codes)
       
    def closeConnection(self):
    
        self.ConnectionBBDD.closeConnection()

    def getDataToCreateModel(self,tableData, columName):

        query = 'SELECT * FROM imathservices."' + tableData + '" where "' + columName + '" = ' + "'" + "0" + "';"
        return self.getQueryMatrixFormat(query)


    def loadModel(self, tableModel, service):
        query = 'select * from imathservices."' + tableModel + '" where "nameModel" = ' + "'" + service + "';"
        return self.getObjectValue(query)


    def getCodeFromModel(self, tableModel, service):
        query = 'select * from imathservices."' + tableModel + '" where "nameModel" = ' + "'" + service + "';"
        return self.getCode(query)

    def getAllData(self, tableData, columnData, value):
        query = 'SELECT * FROM imathservices."' + tableData + '" where "' + columnData + '" = ' + "'" + value + "';"
        return self.getQueryMatrixFormat(query)



