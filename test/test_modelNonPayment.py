from iMathModelosPredictivos.core.modelNonPayment import ModelNonPayment
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier


dataFile = '/home/andrea/MasMovilIbercom/DataAnalysis/entrega2/analisis_impagos/trainData_TwoClass.csv'
m = ModelNonPayment(dataFile, RandomForestClassifier)

modelFile = '/home/andrea/modelos_predictivos/modelo_RandomForest.txt'
m = ModelNonPayment(modelFile)

# testFile = '/home/andrea/MasMovilIbercom/DataAnalysis/entrega2/analisis_impagos/testData_TwoClass.csv'
# outputFile = '/home/andrea/MasMovilIbercom/DataAnalysis/entrega2/analisis_impagos/prediccionDT.csv'

testFile = '/home/andrea/MasMovilIbercom/DataAnalysis/entrega2/analisis_impagos/predictData.csv'
outputFile = '/home/andrea/MasMovilIbercom/DataAnalysis/entrega2/analisis_impagos/realPrediction.csv'

m.predictModel(testFile, outputFile)
