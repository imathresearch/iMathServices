'''
@author: andrea
'''
from iMathModelosPredictivos.core.modelNewCustomer import ModelNewCustomer
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
import os

#list_dir = ['pos_dir', 'pos_ind', 'pre_auto_dir', 'pre_auto_ind', 'pre_clas_dir', 'pre_clas_ind']

list_dir = ['pos_dir']

path = '/home/izubizarreta/Documentos/Documentos/Comercial/MasMovil/Entregable5/entrega4/estudio3'

for d in list_dir:
    dataFile = os.path.join(path, d, 'train.csv')

    m = ModelNewCustomer(dataFile, RandomForestClassifier)

    testFile = os.path.join(path, d, 'test.csv')
    outputFile = os.path.join(path, d, 'evaluation_binary.txt')


    m.testModel(testFile, outputFile)

print "Finished"
