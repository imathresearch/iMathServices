'''
Created on Nov 24, 2015

@author: izubizarreta
'''
from PostgreslManage import PostgreslManage

if __name__ == '__main__':
    
    connection = PostgreslManage("/home/izubizarreta/git/iMathServices/iMathModelosPredictivos/data/ConfigurationValues/ConfigurationValuesPostgresql.txt")
    
    query = 'SELECT * FROM imathservices."Model";'
    
    ListData = connection.getQueryListFormat(query)
    
    print ListData
    
    MatrixData = connection.getQueryMatrixFormat(query)
    
    print MatrixData
    
    maxValue = connection.getPrimaryKey("Model")
    
    print maxValue
    
    connection.closeConnection()