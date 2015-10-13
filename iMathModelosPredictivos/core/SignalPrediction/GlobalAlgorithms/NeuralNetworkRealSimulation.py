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

minutesForEachRoom = [10,15,20]

IntervalTimes = range(5,22,5)

for minutesForEachRoom in minutesForEachRoom:

    '''This algorithm crosses different period of time, 5, 10, 15 or 20 minutes for recovering
    the corresponding data file.'''

    for intervalTime in IntervalTimes:
        
        '''This algorithm crosses different interval of times to get the corresponding file of data.'''

        pathFileTraining = '/home/izubizarreta/Documentos/Documentos/Comercial/Sensovida/SimulacionRealRoberto/Registers' + str(minutesForEachRoom) + str(intervalTime) + 'Training.csv'
        pathFileTest = '/home/izubizarreta/Documentos/Documentos/Comercial/Sensovida/SimulacionRealRoberto/Registers' + str(minutesForEachRoom) + str(intervalTime) + 'Test.csv'
        csvData = CSVClass(pathFileTraining)
        csvDataTest = CSVClass(pathFileTest)

        typeAlgorithms = ['SVC','DecisionTreeClassifier','RandomForestClassifier']

        for typeAlgorithm in typeAlgorithms:

            '''This algorithm calculates different models depending which model is selected'''

            Rooms = [['Salon',0],['Dormitorio',1],['Cocina',2],['Bano',3]]

            for room in Rooms:
    
                key = room[0]
                value = room[1]
    
                rowNumberRoomKey = np.where(csvData.getLabels()==key)
    
                for position in rowNumberRoomKey:
        
                    csvData.setLabel(position, value)

            for room in Rooms:
    
                key = room[0]
                value = room[1]
    
                rowNumberRoomKey = np.where(csvDataTest.getLabels()==key)
    
                for position in rowNumberRoomKey:
        
                    csvDataTest.setLabel(position, value)
    
            ShuffledData = csvData.getData()[1:,:].copy()

            np.random.shuffle(ShuffledData)

            ShuffedDataTest = csvDataTest.getData()[1:,:].copy()

            np.random.shuffle(ShuffedDataTest)

            HeadersAndTraining = []
            HeadersAndTest = []

            element = []
            for header in csvData.getHeaders():
    
                element.append(header)
    
            HeadersAndTraining.append(element)
            HeadersAndTest.append(element)

            for TrainingDataRow in ShuffledData:

                row = []
    
                for element in TrainingDataRow:
                    row.append(element)
    
                HeadersAndTraining.append(row)

            for TestDataRow in ShuffedDataTest:

                row = []
    
                for element in TestDataRow:
                    row.append(element)
    
                HeadersAndTest.append(row)
    
            HeadersAndTraining = np.array(HeadersAndTraining)
            HeadersAndTest = np.array(HeadersAndTest)

            pathTraining = '/home/izubizarreta/Documentos/Documentos/Comercial/Sensovida/SimulacionRealRoberto/Training' + str(minutesForEachRoom) + str(typeAlgorithm) + str(intervalTime) + '.csv' 
            pathTest = '/home/izubizarreta/Documentos/Documentos/Comercial/Sensovida/SimulacionRealRoberto/Test' + str(minutesForEachRoom) + str(typeAlgorithm) + str(intervalTime) + '.csv'

            np.savetxt(pathTraining, HeadersAndTraining, fmt='%s', delimiter=',')
            np.savetxt(pathTest, HeadersAndTest, fmt='%s', delimiter=',')

            notSupervisedModel = ModelPredictUserPosition(pathTraining,eval(typeAlgorithm))
           
            outputFile = '/home/izubizarreta/Documentos/Documentos/Comercial/Sensovida/SimulacionRealRoberto/evaluation_binary' + str(minutesForEachRoom) + str(typeAlgorithm) + str(intervalTime) + '.csv'
            
            notSupervisedModel.testModel(pathTest, outputFile)