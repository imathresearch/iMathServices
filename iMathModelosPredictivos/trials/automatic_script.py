'''
@author: andrea
'''
from iMathModelosPredictivos.core.models.modelGoCustomer import ModelGoCustomer
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
import os

# list_dir = ['pos_dir', 'pos_ind', 'pre_auto_dir', 'pre_auto_ind', 'pre_clas_dir', 'pre_clas_ind']

model = ModelGoCustomer("/home/izubizarreta/git/iMathServices/iMathModelosPredictivos/data/ConfigurationValues/ConfigurationValuesPostgresql.txt","/home/izubizarreta/git/iMathServices/iMathModelosPredictivos/data/ConfigurationValues/ConfigurationValuesElasticsearch.txt","Model","Data","operationData","ChurnCustomer",RandomForestClassifier)

model.saveModel("Model", "ChurnCustomer")

model2 = ModelGoCustomer("/home/izubizarreta/git/iMathServices/iMathModelosPredictivos/data/ConfigurationValues/ConfigurationValuesPostgresql.txt", "/home/izubizarreta/git/iMathServices/iMathModelosPredictivos/data/ConfigurationValues/ConfigurationValuesElasticsearch.txt","Model","Data","operationData","ChurnCustomer")

model2.testModel("resultsModel", "Data", "operationData")

model2.predictModel("resultsModel", "Data", "operationData","telcoresults")

print "Finished"
