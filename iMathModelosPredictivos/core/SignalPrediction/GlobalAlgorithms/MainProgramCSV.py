'''
Created on 2 de oct. de 2015

@author: izubizarreta
'''

from util.CSV import CSVClass
from util.DatesTimes import DatesTimes
from Data.StringOperations import StringOperations
import time
import numpy as np
import math

'''The algorithm crossed the different period of time para crear different data for each one.'''

minutesForEachRoom = [5]

for minuteForEachRoom in minutesForEachRoom:

    pathFileRead = '/home/izubizarreta/Documentos/Documentos/Comercial/Sensovida/SimulacionReal/datosElvira5minutes.csv'
    csvData = CSVClass(pathFileRead)

    # MacCodes = ['0CF3EE00095A','0CF3EE00080B','0CF3EE000598','CF3EE000978']
    MacCodes = ['0CF3EE000A19']
    wpRooms = ['Salon', 'Dormitorio', 'Bano', 'Cocina']
    ConversionNullValues = ['Average', 'Maximum']
    IntervalTime = 10
    Training = 0.8
    Test = 1 - Training
    IntervalTimes = range(10,22,2)
    nullValue = ConversionNullValues[1]
    MaximumValues = -95
    i = 0

    stringOperation = StringOperations()

    for intervalTime in IntervalTimes:

        '''This function grouped same rows depending number of seconds. Initially, it will be
        5 different period of times.'''

        StartData = csvData.getVariables()[0]
        
        GroupData = []
        GroupDataActual = ["Salon", "Dormitorio", "Bano", "Cocina", "Etiqueta"]
        GroupData.append(GroupDataActual)

        GroupDataActual = [0, 0, 0, 0]
        if csvData.getLabels()[0][0] == "":
            GroupDataActual.append("No ubicado")
        else:
            GroupDataActual.append(csvData.getLabels()[0][0])

        GroupData.append(GroupDataActual)

        ElementsByInterval = [0,0,0,0]
        positionElement = 1

        for recover in csvData.getVariables():
    
            # The algorithm does this initial division, because the start row and the first row are the same.
    
            if i > 0:
        
                StringCode = recover[0]
                
                ActualDateString = recover[4]
        
                DateFormatStart = DatesTimes(StartData[4]).getDateFormat()
                DateFormatActual = DatesTimes(ActualDateString).getDateFormat()
        
                # Dates variation. It will be necessary to be sure that they are in the same interval.
        
                DiffDates = time.mktime(DateFormatStart.timetuple()) - time.mktime(DateFormatActual.timetuple())
                
                if DiffDates<0:
                    DiffDates = -1 * DiffDates
      
                # The algorithm adds the actual's row value in the final matrix.
      
                if DiffDates <= intervalTime:
                    MatrixPositionRoom = stringOperation.getPositionMatrix(wpRooms, recover[2])
                    GroupData[positionElement][MatrixPositionRoom] = GroupData[positionElement][MatrixPositionRoom] + float(recover[3])
                    ElementsByInterval[MatrixPositionRoom] = ElementsByInterval[MatrixPositionRoom] + 1
                else:
                    positionMatrix = 0
                    for value in GroupData[positionElement][:-1]:
                        if ElementsByInterval[positionMatrix]==0:
                            GroupData[positionElement][positionMatrix] = float(value)
                        else:
                            GroupData[positionElement][positionMatrix] = float(value) / ElementsByInterval[positionMatrix]
                        positionMatrix = positionMatrix + 1
                    GroupDataActual = [0, 0, 0, 0]
                    positionLabel = np.where(csvData.getData()[:, 0] == recover[0])
                    if csvData.getLabels()[positionLabel[0][0]-1][0] == "":
                        GroupDataActual.append("No ubicado")
                    else:
                        GroupDataActual.append(csvData.getLabels()[positionLabel[0][0]-1][0])
                    MatrixPositionRoom = stringOperation.getPositionMatrix(wpRooms, recover[2])
                    GroupDataActual[MatrixPositionRoom] = GroupDataActual[MatrixPositionRoom] + float(recover[3])
                    GroupData.append(GroupDataActual)
                    if MatrixPositionRoom==0:
                        ElementsByInterval = [1,0,0,0]
                    else:
                        if MatrixPositionRoom==1:
                            ElementsByInterval = [0,1,0,0]
                        else:
                            if MatrixPositionRoom==2:
                                ElementsByInterval = [0,0,1,0]
                            else:
                                ElementsByInterval = [0,0,0,1]
                    StartData = recover
                    positionElement = positionElement + 1
            
            else:
                MatrixPositionRoom = stringOperation.getPositionMatrix(wpRooms, recover[2])
                GroupData[positionElement][MatrixPositionRoom] = GroupData[positionElement][MatrixPositionRoom] + float(recover[3])
                ElementsByInterval[MatrixPositionRoom] = ElementsByInterval[MatrixPositionRoom] + 1
                i = i + 1

        positionMatrix = 0

        for value in GroupData[positionElement][:-1]:
            if ElementsByInterval[positionMatrix]==0:
                GroupData[positionElement][positionMatrix] = float(value)
            else:
                GroupData[positionElement][positionMatrix] = float(value) / ElementsByInterval[positionMatrix]
                positionMatrix = positionMatrix + 1
        
        UserMatrixModels = np.array(GroupData)
        
        np.random.shuffle(UserMatrixModels[1:,:])

        Average = []

        for columns in range(len(UserMatrixModels[0]) - 1):
    
            Rows = np.where(UserMatrixModels[1:, columns].astype(float) < 0)
            if len(Rows[0])>0:
                if float(Rows[0][0]) == 0:
                    Rows = np.delete(Rows[0], 0, 0)
                    Average.append(np.average(UserMatrixModels[Rows, columns][0].astype(float)))
    
            # The following code replace the 0 value for average or maximum. It will be possible to add new options
        
            SelectedColumn = UserMatrixModels[1:, columns]
            if nullValue == 'Average':
                SelectedColumn[SelectedColumn == "0.0"] = str(Average[columns])
                SelectedColumn[SelectedColumn == "0"] = str(Average[columns])
            else:
                if nullValue == 'Maximum':
                    SelectedColumn[SelectedColumn == "0.0"] = MaximumValues
                    SelectedColumn[SelectedColumn == "0"] = MaximumValues
            
            UserMatrixModels[1:, columns] = SelectedColumn
    
        TrainingLength = round(len(UserMatrixModels) * Training)
    
        UserMatrixModelTraining = UserMatrixModels[0:TrainingLength,:]
        UserMatrixModelTest = UserMatrixModels[TrainingLength:,:]  

        pathFileWriteTraining = '/home/izubizarreta/Documentos/Documentos/Comercial/Sensovida/SimulacionReal/Registers' + str(minuteForEachRoom) + str(intervalTime) + 'Training.csv'
        pathFileWriteTest = '/home/izubizarreta/Documentos/Documentos/Comercial/Sensovida/SimulacionReal/Registers' + str(minuteForEachRoom) + str(intervalTime) + 'Test.csv'
    
        np.savetxt(pathFileWriteTraining, UserMatrixModelTraining, fmt='%s', delimiter=',')
        np.savetxt(pathFileWriteTest, UserMatrixModelTest, fmt='%s', delimiter=',')