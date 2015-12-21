"""
    Implements the class ElasticsearchClass , a class to work with the elasticsearch database
Authors:
@author iMath
"""
from elasticsearch import Elasticsearch
from iMathModelosPredictivos.common.util.jsonOperations import jsonOperations
from iMathModelosPredictivos.common.util.ReadConfigurationData import ConfigurationData
from iMathModelosPredictivos.common.constants import CONS

CONS = CONS()

class ElasticsearchClass(object):
    '''
    classdocs
    '''


    def __init__(self, host, port):
        '''
        Constructor
        '''
        self.elasticsearch = Elasticsearch(self.getConnectionString(host,port))
        
    def getConnectionString(self,host,port):
        
        return [{'host': host, 'port': port}]


        
    def getRequestBody(self,service):
        if service == 'ChurnCustomer':
            request_body = CONS.PROPERTIES_INDEX_ELASTIC_CHURN_CUSTOMER
        elif service == 'DownEmployee':
            request_body = CONS.PROPERTIES_INDEX_ELASTIC_DOWN_EMPLOYEE
        return request_body
        
    def deleteAndCreateDictionary(self,dictionary,service):
        
        if self.elasticsearch.indices.exists(dictionary):
            res = self.elasticsearch.indices.delete(index = dictionary)
            
        res = self.elasticsearch.indices.create(index = dictionary, body = self.getRequestBody(service))

    def createDictionary(self,dictionary):
        
        res = self.elasticsearch.indices.create(index = dictionary, body = self.getRequestBody())

    def setDeleteDictionary(self,dictionary):
        
        res = self.elasticsearch.indices.delete(index = dictionary)
        
    def getJsonStructure(self,model, codes, labels,probabilities,service):
        
        jsonStructure = jsonOperations()
        dataJSONFormat = jsonStructure.getResultsDict(model, codes, labels, probabilities,service)
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

    def setElementsWithBulk(self,dictionary,listElements):
        bulk_data=[]
        inc=0
        for row in listElements:
            inc+=1
            op_dict = {
                "index": {
                    "_index": dictionary,
                    "_type": 'blog',
                    "_id": inc
                }
            }
            bulk_data.append(op_dict)
            bulk_data.append(row)

        self.elasticsearch.bulk(index = dictionary, body = bulk_data, refresh = True)


    def setResults(self,dictionary,labels,probabilities):
        
        res = self.elasticsearch.bulk(index = dictionary, body = self.getJsonStructure(labels, probabilities), refresh = True)


