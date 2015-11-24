'''
@author: inigo
'''
from iMathModelosPredictivos.core.modelDownEmployee import ModelDownEmployee
from sklearn.tree import DecisionTreeClassifier
from iMathModelosPredictivos.common.constants import CONS
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
import os

# list_dir = ['pos_dir', 'pos_ind', 'pre_auto_dir', 'pre_auto_ind', 'pre_clas_dir', 'pre_clas_ind']

list_dir = ['DataConversionNumeros']

path = '/home/izubizarreta/Data/'

methods = ['DecisionTreeClassifier', 'SVC', 'RandomForestClassifier']

position = 0
        
for method in methods:
            
    finalPath = path + 'HREmployeeAttritionTrain.csv'

    dataFile = finalPath

    print dataFile
                
    methodclass = eval(method)

    m = ModelDownEmployee(dataFile, methodclass)
                    
    '''CONS = CONS()
                    
    m.saveModel(CONS.MODEL_FILE_LOCATION + "Down" + '.txt')'''
            
    characters = 'WithoutChange'

    finalPath = path + 'HREmployeeAttritionTest.csv'
            
    outputFile = path + 'HREmployeeAttritionOutput.csv'
            
    m.testModel(finalPath, outputFile)

print "Finished"
