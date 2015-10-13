'''
Created on 2 de oct. de 2015

@author: izubizarreta
'''

from util.CSVDatosRoberto import CSVClass
import numpy as np
import math
from NeuralNetworkTemplate.PredictUserPosition import ModelPredictUserPosition
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

pathFileRead = '/home/izubizarreta/Documentos/Documentos/Comercial/Sensovida/PruebasInicialesWrite.csv'
csvData = CSVClass(pathFileRead)

PercentageTraining = 80
PercentageTest = 20

Rooms = [['Salon',0],['Dormitorio',1],['Bano',2],['Cocina',3]]

for room in Rooms:
    
    key = room[0]
    value = room[1]
    
    rowNumberRoomKey = np.where(csvData.getLabels()==key)
    
    for position in rowNumberRoomKey:
        
        csvData.setLabel(position, value)
    
ShuffledData = csvData.getData()[1:,:].copy()

np.random.shuffle(ShuffledData)

TrainingDataLength = np.round(len(ShuffledData[:,0]) * (float(PercentageTraining)/100))

TrainingData = ShuffledData[0:TrainingDataLength,:]

TestData = ShuffledData[TrainingDataLength:,:]

HeadersAndTraining = []
HeadersAndTest = []

element = []
for header in csvData.getHeaders():
    
    element.append(header)
    
HeadersAndTraining.append(element)
HeadersAndTest.append(element)

for TrainingDataRow in TrainingData:

    row = []
    
    for element in TrainingDataRow:
        row.append(element)
    
    HeadersAndTraining.append(row)

for TestDataRow in TestData:

    row = []
    
    for element in TestDataRow:
        row.append(element)
    
    HeadersAndTest.append(row)
    
HeadersAndTraining = np.array(HeadersAndTraining)
HeadersAndTest = np.array(HeadersAndTest)

np.savetxt('../Data/Training.csv', HeadersAndTraining, fmt='%s', delimiter=',')
np.savetxt('../Data/Test.csv', HeadersAndTest, fmt='%s', delimiter=',')

notSupervisedModel = ModelPredictUserPosition('../Data/Training.csv',eval('SVC'))

finalPath = '../Data/Test.csv'
            
outputFile = '../Data/evaluation_binary.csv'
            
notSupervisedModel.testModel(finalPath, outputFile)