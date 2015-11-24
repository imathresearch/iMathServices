'''
Created on 2 de oct. de 2015

@author: izubizarreta
'''


from iMathModelosPredictivos.core.SignalPrediction.util.CSV import CSVClass
from iMathModelosPredictivos.common.util.ConnectionBBDDMysql import ConnectionBBDD
from iMathModelosPredictivos.core.SignalPrediction.util.DatesTimes import DatesTimes
from iMathModelosPredictivos.core.SignalPrediction.Data.StringOperations import StringOperations
from iMathModelosPredictivos.core.modelPredictPosition import ModelPredictUserPosition
from iMathModelosPredictivos.core.SignalPrediction.Classes.NeuralNetworkCalculation import NeuralNetworkCalculation
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from time import gmtime, strftime
import time
import numpy as np
import math

'''The algorithm crossed the different period of time para crear different data for each one.'''

class FilterData(object):
    
    def getConnection(self):
        
        userConnection = ConnectionBBDD()
        self.userConnection = userConnection

    def RecoverData(self, path):
        
        # self.userConnection.userConnection.DoConnection()
        # RecoverData = self.userConnection.userConnection.getResults(query, ['id', 'user_id', 'wp', 'rssi', 'datetime', 'real_location'])
        csvData = CSVClass(path)
        return csvData
    
    def FilterExecution(self, calibracion, grupotiempo, maximosenal, path, pathResult, operation):

        minutesForEachRoom = [calibracion]

        for minuteForEachRoom in minutesForEachRoom:

            # startDate = '2015-09-30 17:30:00'
            # endDate = '2015-10-01 11:00:00'

            MacCodes = ['0CF3EE000A19']

            # query = 'SELECT * FROM sensovida_panel_validacion.beacon_test' 
            # query = query + ' where datetime > "' + startDate + '" and datetime < "' + endDate + '"'
            # query = query + ' and user_id="' + MacCodes[0] + ')'
            # query = query + ' order by datetime desc'
            
            # self.getConnection()
            
            csvData = self.RecoverData(path)

            # MacCodes = ['0CF3EE00095A','0CF3EE00080B','0CF3EE000598','CF3EE000978']
            wpRooms = ['salon', 'dormitorio', 'bano', 'cocina']
            ConversionNullValues = ['Average', 'Maximum']
            IntervalTimes = [grupotiempo]
            nullValue = ConversionNullValues[1]
            MaximumValues = maximosenal
            i = 0

            stringOperation = StringOperations()

            for intervalTime in IntervalTimes:

                '''This function grouped same rows depending number of seconds. Initially, it will be
                5 different period of times.'''

                StartData = csvData.getVariables()[0]
        
                GroupData = []
                GroupDataActual = ["salon", "dormitorio", "bano", "cocina", "etiqueta"]
                GroupData.append(GroupDataActual)

                GroupDataActual = [0, 0, 0, 0]
                if csvData.getLabels()[0][0] == "":
                    GroupDataActual.append("No ubicado")
                else:
                    GroupDataActual.append(csvData.getLabels()[0][0])

                GroupData.append(GroupDataActual)

                ElementsByInterval = [0, 0, 0, 0]
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
                
                        if DiffDates < 0:
                            DiffDates = -1 * DiffDates
      
                        # The algorithm adds the actual's row value in the final matrix.
      
                        if DiffDates <= intervalTime:
                            MatrixPositionRoom = stringOperation.getPositionMatrix(wpRooms, recover[2])
                            GroupData[positionElement][MatrixPositionRoom] = GroupData[positionElement][MatrixPositionRoom] + float(recover[3])
                            ElementsByInterval[MatrixPositionRoom] = ElementsByInterval[MatrixPositionRoom] + 1
                        else:
                            positionMatrix = 0
                            for value in GroupData[positionElement][:-1]:
                                if ElementsByInterval[positionMatrix] == 0:
                                    GroupData[positionElement][positionMatrix] = float(value)
                                else:
                                    GroupData[positionElement][positionMatrix] = float(value) / ElementsByInterval[positionMatrix]
                                positionMatrix = positionMatrix + 1
                            GroupDataActual = [0, 0, 0, 0]
                            positionLabel = np.where(csvData.getData()[:, 0] == recover[0])
                            if csvData.getLabels()[positionLabel[0][0] - 1][0] == "":
                                GroupDataActual.append("No ubicado")
                            else:
                                GroupDataActual.append(csvData.getLabels()[positionLabel[0][0] - 1][0])
                            MatrixPositionRoom = stringOperation.getPositionMatrix(wpRooms, recover[2])
                            GroupDataActual[MatrixPositionRoom] = GroupDataActual[MatrixPositionRoom] + float(recover[3])
                            GroupData.append(GroupDataActual)
                            if MatrixPositionRoom == 0:
                                ElementsByInterval = [1, 0, 0, 0]
                            else:
                                if MatrixPositionRoom == 1:
                                    ElementsByInterval = [0, 1, 0, 0]
                                else:
                                    if MatrixPositionRoom == 2:
                                        ElementsByInterval = [0, 0, 1, 0]
                                    else:
                                        ElementsByInterval = [0, 0, 0, 1]
                            StartData = recover
                            positionElement = positionElement + 1
            
                    else:
                        MatrixPositionRoom = stringOperation.getPositionMatrix(wpRooms, recover[2])
                        GroupData[positionElement][MatrixPositionRoom] = GroupData[positionElement][MatrixPositionRoom] + float(recover[3])
                        ElementsByInterval[MatrixPositionRoom] = ElementsByInterval[MatrixPositionRoom] + 1
                        i = i + 1

                positionMatrix = 0

                for value in GroupData[positionElement][:-1]:
                    if ElementsByInterval[positionMatrix] == 0:
                        GroupData[positionElement][positionMatrix] = float(value)
                    else:
                        GroupData[positionElement][positionMatrix] = float(value) / ElementsByInterval[positionMatrix]
                    positionMatrix = positionMatrix + 1
        
                UserMatrixModels = np.array(GroupData)
            
            self.setChangeMaximum(UserMatrixModels, nullValue, MaximumValues)
            
            if operation == 2:
                
                UserMatrixModels = UserMatrixModels[:, :-1]
                
            else:
                
                np.random.shuffle(UserMatrixModels[1:, :])
    
                '''This algorithm calculates different models depending which model is selected'''
            
                Rooms = [['salon', 0], ['dormitorio', 1], ['bano', 2], ['cocina', 3]]

                UserMatrixModels = self.getChangeLabel(Rooms, UserMatrixModels)
            
            np.savetxt(pathResult, UserMatrixModels, fmt='%s', delimiter=',')
            
            return UserMatrixModels
                    

    def setStoreTrainingTest(self, UserMatrixModels, Training, pathTraining, pathTest):

        # shuffledData = self.getDataShuttfled(UserMatrixModelTraining, UserMatrixModelTest)
        TrainingLength = round(len(UserMatrixModels) * Training)
        
        DataSeparated = self.getTrainingTestData(UserMatrixModels, TrainingLength)
            
        np.savetxt(pathTraining, DataSeparated[0], fmt='%s', delimiter=',')
        np.savetxt(pathTest, DataSeparated[1], fmt='%s', delimiter=',')
            
    def getTrainingTestData(self, UserMatrixModels, TrainingLength):                    
   
        UserMatrixModelTraining = UserMatrixModels[0:TrainingLength, :]
        UserMatrixModelTestHeader = UserMatrixModels[0, :]        
        UserMatrixModelTestData = UserMatrixModels[TrainingLength:, :]
        # UserMatrixModelTest = np.vstack(UserMatrixModelTestHeader,UserMatrixModelTestData)
        DataTest = []
        DataTestRow = []
        for value in UserMatrixModelTestHeader:
            DataTestRow.append(value)
        DataTest.append(DataTestRow)
        for row in UserMatrixModelTestData:
            DataTestRow = []
            for column in row:
                DataTestRow.append(column)
            DataTest.append(DataTestRow)
        UserMatrixModelTest = np.asarray(DataTest, dtype="|S50")
        return [UserMatrixModelTraining, UserMatrixModelTest]
    
    def setChangeMaximum(self, UserMatrixModels, nullValue, MaximumValues):
        
        Average = []

        for columns in range(len(UserMatrixModels[0]) - 1):
    
            Rows = np.where(UserMatrixModels[1:, columns].astype(float) < 0)
            if len(Rows[0]) > 0:
                if float(Rows[0][0]) == 0:
                    Rows = np.delete(Rows[0], 0, 0)
                    Average.append(np.average(UserMatrixModels[Rows, columns][0].astype(float)))
        
            SelectedColumn = UserMatrixModels[1:, columns]
            if nullValue == 'Average':
                SelectedColumn[SelectedColumn == "0.0"] = str(Average[columns])
                SelectedColumn[SelectedColumn == "0"] = str(Average[columns])
            else:
                if nullValue == 'Maximum':
                    SelectedColumn[SelectedColumn == "0.0"] = MaximumValues
                    SelectedColumn[SelectedColumn == "0"] = MaximumValues
            
            UserMatrixModels[1:, columns] = SelectedColumn
            
        return UserMatrixModels

    
    def getChangeLabel(self, Rooms, UserMatrixModels):
        
        rowNumberRoomKey = np.where(UserMatrixModels[1:, -1:] == 'salon')
        for position in rowNumberRoomKey:
            UserMatrixModels[position + 1, -1:] = 0

        rowNumberRoomKey = np.where(UserMatrixModels[1:, -1:] == 'dormitorio')
        for position in rowNumberRoomKey:
            UserMatrixModels[position + 1, -1:] = 1

        rowNumberRoomKey = np.where(UserMatrixModels[1:, -1:] == 'bano')
        for position in rowNumberRoomKey:
            UserMatrixModels[position + 1, -1:] = 2

        rowNumberRoomKey = np.where(UserMatrixModels[1:, -1:] == 'cocina')
        for position in rowNumberRoomKey:
            UserMatrixModels[position + 1, -1:] = 3

        UserMatrixModels[0, -1:] = 'etiqueta'

        return UserMatrixModels

    
    def getDataShuttfled(self, UserMatrixModelTraining, UserMatrixModelTest):
        
        ShuffledData = UserMatrixModelTraining.copy()
        np.random.shuffle(ShuffledData)
        ShuffedDataTest = UserMatrixModelTest.copy()
        np.random.shuffle(ShuffedDataTest)
        return [ShuffledData, ShuffedDataTest]
    
    def _storeDataModel(self, id, NameModel, BeaconMac):
            
        max = self.userConnection.getNextPrimaryKey("beacon_test_model")
        self.model_id = max
        parameters = [max, NameModel, id, BeaconMac, 'RandomForest', 15, 5, strftime("%Y-%m-%d %H:%M:%S", gmtime())]
        self.userConnection.setDataModel("beacon_test_model", parameters)
        
    def _storeDataModelData(self, data):
            
        self.userConnection.setDataModelData("beacon_test_data", self.model_id, data)
