'''
Created on 1 de oct. de 2015

@author: izubizarreta
'''

from iMathModelosPredictivos.common.util.ReadConfigurationData import ConfigurationData
import psycopg2
import numpy as np




class ConnectionBBDD(object):
    '''
    classdocs
    '''


    def __init__(self, host, user, password, database):
        '''
        Constructor
        '''
        
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        connectstring = "host=" + self.host + " " + "user=" + self.user + " " + "password=" + self.password + " dbname=" + self.database
        self.db = psycopg2.connect(connectstring)

        
    def getFetch(self, query):
        
        cursor = self.db.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        return results
        
    def getResultsList(self, query):
                
        results = self.getFetch(query)
        AllData = []
        for result in results:
            Data = []
            for element in result:
                Data.append(element)
            AllData.append(Data)
        return AllData
        
    def getResults(self, query):
        
        results = self.getFetch(query)
        AllData = []
        for result in results:
            Data = []
            for element in result:
                Data.append(element)
            AllData.append(Data)
        AllData = np.asarray(AllData, dtype="|S50")
        return AllData
    
    def getObjectData(self,query):
        
        results = self.getFetch(query)
        return results[0][2]
    
    def getCode(self,query):
        
        results = self.getFetch(query)
        if len(results)==0:
            return 1
        else:
            return results[0][0]
    
    def getNextPrimaryKey(self, table):
        
        query = self.getMaxValueTable(table)
        results = self.getFetch(query)
        max = 0
        if str(results[0][0])!='None':
            for result in results:
                max = result[0]
        max = max + 1
        return max
    
    def getExist(self, table, serviceValue):
        
        query = 'select count(*) from imathservices."' + table + '" where "nameModel" = ' + "'" + serviceValue + "';"
        results = self.getFetch(query)
        for result in results:
            exist = result[0]
        return exist
        
    def getColumnNames(self,table):
        
        query = "SELECT column_name FROM information_schema.columns where table_name = '" + table + "' order by ordinal_position;"
        MatrixData = self.getResults(query)
        return MatrixData
    
    def getColumnTrain(self,table):
        
        MatrixData = self.getColumnNames(table)
        return MatrixData[1:-1]
    
    def getColumnTest(self,table):
        
        MatrixData = self.getColumnNames(table)
        return MatrixData[1:-1]

    def getColumnPredict(self,table):
        
        MatrixData = self.getColumnNames(table)
        return MatrixData[0:-2]    

    def setDataModel(self, table, parameters, serviceValue):
        
        '''This functions stores information about the model'''
        
        cursor = self.db.cursor()
        
        exist = self.getExist(table, serviceValue)
        
        if exist==0:
        
            query =  'INSERT INTO imathservices."' + table + '" VALUES (%s, %s, %s, %s, %s, %s);'
            cursor.execute(query, parameters)
        
        else:
            
            parametersStore = [parameters[2],parameters[3],parameters[4],str(parameters[5]),parameters[1]]
            cursor.execute('UPDATE imathservices."' + table + '" SET "serializationValue"=%s,"trainingPercentage"=%s,"testPercentage"=%s,"createDate"=%s WHERE "nameModel"=%s', parametersStore)
        
        self.db.commit()
        
    def setDataModelResults(self, operation, table, data, probabilities, codes):
        
        '''This functions stores information about the models results'''
        
        cursor = self.db.cursor()
        position = 0
        
        for eachdata in data:         

            probabilityValues = ''
            for probability in probabilities[position]:
                probabilityValues = probabilityValues + str(probability) + ","
                    
            probabilityValues = probabilityValues[:-1]
            
            if operation==0:
                
                typeOperation = 'test'
                
            else:
                
                typeOperation = 'prediction'
            
            confusionMatrixValues = ''
            for confusionMatrix in codes[4]:
                confusionMatrixValues = confusionMatrixValues + str(confusionMatrix) + ","
                
            confusionMatrixValues = confusionMatrixValues[:-1]
                        
            dataInsert = [codes[0]+position,codes[1],operation,eachdata,probabilityValues,str(confusionMatrixValues),str(codes[2][position]),str(codes[3])]
                                   
            query =  'INSERT INTO imathservices."' + table + '" VALUES (%s, %s, %s, %s, %s, %s, %s, %s);'
            cursor.execute(query, dataInsert)
            
            self.db.commit()
            
            position = position + 1       
            
    def closeConnection(self):
        
        self.db.close()
        return 0


    def getMaxValueTable(self, table):
        
        return 'select max(id) from imathservices."' + table + '";'