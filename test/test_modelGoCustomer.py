'''
@author: inigo
'''
from iMathModelosPredictivos.core.modelGoCustomer import ModelGoCustomer
from sklearn.tree import DecisionTreeClassifier
from iMathModelosPredictivos.common.constants import CONS
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
import os

# list_dir = ['pos_dir', 'pos_ind', 'pre_auto_dir', 'pre_auto_ind', 'pre_clas_dir', 'pre_clas_ind']

list_dir = ['DataConversionNumeros']

path = '/home/izubizarreta/Documentos/Documentos/Comercial/MasMovil/Entregable6/Data/'

CONS = CONS()

months = [11]

typeCanal = ['Ext']

terminacionCode = ['']

charactersValues = ['WithoutChange']

methods = ['DecisionTreeClassifier', 'SVC', 'RandomForestClassifier']

position = 0

for dir in list_dir:

    for typecanal in typeCanal:
        
        for charactersvalues in charactersValues:
            
            for terminacioncode in terminacionCode:
            
                for method in methods:
            
                    charactersTrain = charactersvalues

                    finalPath = path + dir + '/' + 'train' + str(terminacioncode) + str(typecanal) + str(charactersTrain) + '.csv'

                    dataFile = finalPath

                    print dataFile
                
                    methodclass = eval(method)

                    m = ModelGoCustomer(dataFile, methodclass)
                                       
                    m.saveModel(CONS.MODEL_FILE_LOCATION + "Go" + '.txt')
                    
                    newm = ModelGoCustomer(CONS.MODEL_FILE_LOCATION + "Go" + '.txt')
            
                    characters = 'WithoutChange'

                    finalPath = path + dir + '/' + 'test' + str(terminacioncode) + str(typecanal) + str(charactersTrain) + '.csv'
            
                    outputFile = path + dir + '/' + 'result' + str(terminacioncode) + str(typecanal) + str(charactersTrain) + str(method) + 'evaluation_binary.csv'
            
                    m.testModel(finalPath, outputFile)
                    
                    finalPath = path + dir + '/' + 'predict' + str(terminacioncode) + str(typecanal) + str(charactersTrain) + '.csv'
                    
                    outputFile = path + dir + '/' + 'result' + str(terminacioncode) + str(typecanal) + str(charactersTrain) + str(method) + 'predict_evaluation_binary.csv'
                    
                    newm.predictModel(finalPath, outputFile)

print "Finished"

'''for d in list_dir:

    dataFile = os.path.join(path, d, 'train.csv')

    m = ModelNewCustomer(dataFile, RandomForestClassifier)

    testFile = os.path.join(path, d, 'test.csv')
    outputFile = os.path.join(path, d, 'evaluation_binary.txt')


    m.testModel(testFile, outputFile)

print "Finished"'''
