'''
Created on Nov 26, 2015

@author: izubizarreta
'''
from elasticsearch import Elasticsearch
from iMathModelosPredictivos.common.util.jsonOperations import jsonOperations
from iMathModelosPredictivos.common.util.ReadConfigurationData import ConfigurationData
import numpy as np

class ElasticsearchClass(object):
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
        self.port = ConnectionsValues[1]
        
    def getConnectionString(self):
        
        connection = [{'host': self.host, 'port': self.port}]
        return connection
    
    def createConnection(self):
        
        self.elasticsearch = Elasticsearch(self.getConnectionString())
        
    def getRequestBody(self):
        
        request_body = {
                        "settings" : {
                                      "number_of_shards": 1,
                                      "number_of_replicas": 0
                                      }
                        }
        return request_body
        
    def deleteAndCreateDictionary(self,dictionary):
        
        if self.elasticsearch.indices.exists(dictionary):
            res = self.elasticsearch.indices.delete(index = dictionary)
            
        res = self.elasticsearch.indices.create(index = dictionary, body = self.getRequestBody())

    def createDictionary(self,dictionary):
        
        res = self.elasticsearch.indices.create(index = dictionary, body = self.getRequestBody())

    def setDeleteDictionary(self,dictionary):
        
        res = self.elasticsearch.indices.delete(index = dictionary)
        
    def getJsonStructure(self,model, codes, labels,probabilities):
        
        jsonStructure = jsonOperations()
        dataJSONFormat = jsonStructure.getResultsDict(model, codes, labels, probabilities)
        return dataJSONFormat
    
    def setElement(self,dictionary,position,bodyValue):
        
        self.elasticsearch.index(index=dictionary, doc_type='blog', id=position, body=bodyValue)
        
    def getElement(self,dictionary, position):
        
        element = self.elasticsearch.get(index=dictionary, doc_type='blog', id=position)
        return element
    
    def setElements(self,dictionary,listElements):
        
        elementPosition = 0
        for bodyValue in listElements:
            elementPosition = elementPosition + 1
            self.setElement(dictionary, elementPosition, bodyValue)
        return 0
        
    def setResults(self,dictionary,labels,probabilities):
        
        res = self.elasticsearch.bulk(index = dictionary, body = self.getJsonStructure(labels, probabilities), refresh = True)