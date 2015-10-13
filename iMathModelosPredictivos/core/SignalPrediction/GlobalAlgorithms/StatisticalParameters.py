'''
Created on 5 de oct. de 2015

@author: izubizarreta
'''

from iMathModelosPredictivos.core.SignalPrediction.util.CSV import CSVClass
import numpy as np

pathFileReadGood = '/home/izubizarreta/Documentos/Documentos/Comercial/Sensovida/DataGoodPrediction.csv'
pathFileReadBad = '/home/izubizarreta/Documentos/Documentos/Comercial/Sensovida/DataBadPrediction.csv'

pathFileWriteGood = '/home/izubizarreta/Documentos/Documentos/Comercial/Sensovida/DataGoodPredictionStatictis'
pathFileWriteBad = '/home/izubizarreta/Documentos/Documentos/Comercial/Sensovida/DataBadPredictionStatics'

paths = [pathFileWriteGood, pathFileWriteBad]

wpRooms = ['Salon', 'Dormitorio', 'Bano', 'Cocina']

csvDataGood = CSVClass(pathFileReadGood)
csvDataBad = CSVClass(pathFileReadBad)

position = 0

csvFiles = [csvDataGood, csvDataBad]

for csvs in csvFiles:
    
    for room in wpRooms:
        
        StatictalParameters = []
    
        indexEachRoom = np.where(csvs.getLabels()==room)

        for column in range(len(csvs.getVariables()[0])):
    
            ActualStatisticalValues =[]
    
            ValuesActualColumn = csvDataGood.getVariables()[indexEachRoom,:][0][:,column]
    
            ValuesActualColumn = ValuesActualColumn.astype(float)
    
            mean = np.mean(ValuesActualColumn)
            var = np.var(ValuesActualColumn)
            std = np.std(ValuesActualColumn)
            max = np.max(ValuesActualColumn)
            min = np.min(ValuesActualColumn)
            percentile95 = np.percentile(ValuesActualColumn, 95)
            confidenceInterval95Minimum = mean - (2 * std)
            confidenceInterval95Maximum = mean + (2 * std)
            confidenceInterval995Minimum = mean - (3 * std)
            confidenceInterval995Maximum = mean + (3 * std)
            
            ActualStatisticalValues.append(mean)
            ActualStatisticalValues.append(var)
            ActualStatisticalValues.append(std)
            ActualStatisticalValues.append(max)
            ActualStatisticalValues.append(min)
            ActualStatisticalValues.append(percentile95)
            ActualStatisticalValues.append(confidenceInterval95Minimum)
            ActualStatisticalValues.append(confidenceInterval95Maximum)
            ActualStatisticalValues.append(confidenceInterval995Minimum)
            ActualStatisticalValues.append(confidenceInterval995Maximum)


            StatictalParameters.append(ActualStatisticalValues)
        
        pathWrite = paths[position] + room + ".csv"        
        np.savetxt(pathWrite, StatictalParameters, fmt='%s', delimiter=',')
        
    position = position + 1