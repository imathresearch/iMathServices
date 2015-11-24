'''
Created on 1 de oct. de 2015

@author: izubizarreta
'''

from iMathModelosPredictivos.common.util.ReadConfigurationData import ConfigurationData
import psycopg2
import numpy as np
from _mysql import result

class ConnectionBBDD(object):
    '''
    classdocs
    '''


    def __init__(self, path):
        '''
        Constructor
        '''
        connectBBDD = ConfigurationData()
        
        ConnectionsValues = connectBBDD.getData(path)
        
        self.host = ConnectionsValues[0]
        self.user = ConnectionsValues[1]
        self.password = ConnectionsValues[2]
        self.database = ConnectionsValues[3]
        
    def DoConnection(self):
        
        connectstring = "host=" + self.host + " " + "user=" + self.user + " " + "password=" + self.password + "dbname=" + self.database        
        self.db = psycopg2.connect(connectstring)
        
    def getFetch(self, query):
        
        cursor = self.db.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        return results
        
    def getResultsList(self, query, headers):
        
        results = self.getFetch(query)
        AllData = []
        AllData.append(headers)
        for result in results:
            Data = []
            for element in result:
                Data.append(element)
            AllData.append(Data)
        return AllData
        
    def getResults(self, query, headers):
        
        results = self.getFetch(query)
        AllData = []
        AllData.append(headers)
        for result in results:
            Data = []
            for element in result:
                Data.append(element)
            AllData.append(Data)
        AllData = np.asarray(AllData, dtype="|S50")
        return AllData

    def getNextPrimaryKey(self, table):
        
        query = self.getMaxValueTable(table)
        results = self.getFetch(query)
        for result in results:
            max = result[0]
        max = max + 1
        return max

    def setDataModel(self, table, parameters):
        
        '''This functions stores information about the model'''
        
        cursor = self.db.cursor()        
        
        self.db.commit()
        
    def setDataModelResults(self, table, data):
        
        '''This functions stores information about the models results'''
        
        cursor = self.db.cursor()
        
        for eachdata in data:            
        
            self.db.commit()        
            
    def closeConnection(self):
        
        self.db.close()
        return 0


    def getMaxValueTable(self, table):
        
        return "select max(id) from " + table
