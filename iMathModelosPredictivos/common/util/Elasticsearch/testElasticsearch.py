'''
Created on Nov 26, 2015

@author: izubizarreta
'''
from ElasticsearchClass import ElasticsearchClass

if __name__ == '__main__':
    
    es = ElasticsearchClass("/home/izubizarreta/git/iMathServices/iMathModelosPredictivos/data/ConfigurationValues/ConfigurationValuesElasticsearch.txt")
    es.createConnection()
    es.deleteAndCreateDictionary("telcoresults")
    body = {"query": {"fuzzy_like_this_field" : { "name" : {"like_text": "jaba", "max_query_terms":5}}}}
    elementPosition = 1 
    es.setElement("telco",elementPosition,body)
    element = es.getElement("telco",elementPosition)
    print element
    allbody = []
    for value in range(1,10):
        body = {"query": {"fuzzy_like_this_field" : { "name" : {"like_text": "jaba", "max_query_terms":5}}}}
        allbody.append(body)    
    for bodyValue in allbody:
        elementPosition = elementPosition + 1
        es.setElement("telco", elementPosition, bodyValue)
    element = es.getElement("telco",elementPosition-4)
    print element