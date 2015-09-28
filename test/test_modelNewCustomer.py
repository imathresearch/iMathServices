'''
Created on 18/06/2015

@author: andrea
'''
from iMathModelosPredictivos.core.modelNewCustomer import ModelNewCustomer
from iMathModelosPredictivos.common.constants import CONS
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

CONS = CONS()

#dataFile = '/home/andrea/MasMovilIbercom/DataAnalysis/entrega4/estudio3/pre_auto_ind/train.csv'
#m = ModelNewCustomer(dataFile, RandomForestClassifier)
#m.saveModel(CONS.MODEL_FILE_LOCATION + 'test_model1.txt');

model = ModelNewCustomer(CONS.MODEL_FILE_LOCATION + 'test_model1.txt');
#predictFile ='/home/andrea/MasMovilIbercom/DataAnalysis/entrega4/estudio3/pre_auto_ind/predict.csv'
#outputFile = '/home/andrea/MasMovilIbercom/DataAnalysis/entrega4/estudio3/pre_auto_ind/prediccion1.txt'
#model.predictModel(predictFile, outputFile);


#modelFile = '/home/andrea/modelos_predictivos/modelo_RandomForest.txt'
#m = ModelNewCustomer(modelFile)


testFile = '/home/andrea/MasMovilIbercom/DataAnalysis/entrega4/estudio3/pre_auto_ind/test.csv'
outputFile = '/home/andrea/MasMovilIbercom/DataAnalysis/entrega4/estudio3/pre_auto_ind/evaluation_prop.txt'
model.testModel(testFile, outputFile)
#predictFile ='/home/andrea/MasMovilIbercom/DataAnalysis/entrega4/estudio3/pre_auto_ind/predict.csv'
#outputFile = '/home/andrea/MasMovilIbercom/DataAnalysis/entrega4/estudio3/pre_auto_ind/prediccion.txt'
#m.predictModel(predictFile, outputFile)