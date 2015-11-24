'''
Created on 1 de oct. de 2015

@author: izubizarreta
'''

from ReadConfigurationData import ConfigurationData
import MySQLdb
import numpy as np
from time import gmtime, strftime 

class ConnectionBBDD(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        connectBBDD = ConfigurationData()
        
        ConnectionsValues = connectBBDD.getData()
        
        self.host = ConnectionsValues[0]
        self.user = ConnectionsValues[1]
        self.password = ConnectionsValues[2]
        self.database = ConnectionsValues[3]
        
    def DoConnection(self):
        
        self.db = MySQLdb.connect(self.host, self.user, self.password, self.database)
        
    def getResults(self, query, headers):
        
        cursor = self.db.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
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
        
        cursor = self.db.cursor()
        query = "select max(id) from " + table
        cursor.execute(query)
        results = cursor.fetchall()
        for result in results:
            max = result[0]
        max = max + 1
        return max

    def setDataModel(self, table, parameters):
        
        cursor = self.db.cursor()

        add_employee = ("INSERT INTO " + table + " VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

        data_employee = []
        
        for parameter in parameters:
            data_employee.append(parameter)

        cursor.execute(add_employee, data_employee)
        
        self.db.commit()
        
    def setDataModelData(self, model_id, table, prediction, probabilities):
        
        cursor = self.db.cursor()
        
        for eachPrediction in prediction:
            
            max = self.getNextPrimaryKey(table)

            add_employee = ("INSERT INTO " + table + " (id,model_id,salon,dormitorio,cocina,bano,predicted_tag,execution_type,datetime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")

            data_employee = [max, model_id]
        
            for probability in probabilities:
                data_employee.append(probability)

            data_employee.append(eachPrediction)
            
            data_employee.append('Prediction')
            
            data_employee.append(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

            cursor.execute(add_employee, data_employee)
        
            self.db.commit()        
            
    def closeConnection(self):
        
        self.db.close()
        return 0
