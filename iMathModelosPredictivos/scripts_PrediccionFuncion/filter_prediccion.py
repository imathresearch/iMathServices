#!/usr/bin/env python

import sys
import os

from iMathModelosPredictivos.core.SignalPrediction.Data.constants import CONS

from iMathModelosPredictivos.core.SignalPrediction.Classes.FilterData import FilterData

CONS = CONS()

try:
                      
    # Check the number of parameters
    '''if len(sys.argv) != 4:
        print "Numero de parametros incorrectos"
    
    dataFile = sys.argv[1]
    classifierType = sys.argv[2]
    modelName = sys.argv[3]'''
    
    operation = 1

    #Initial Data

    dataFile = '/home/izubizarreta/Documentos/Documentos/Comercial/Sensovida/DatosEduardo/DatosEduardo.csv'
    
    #Filtered data
    
    DataFiltered = FilterData()
    
    pathResult = '/home/izubizarreta/Documentos/Documentos/Comercial/Sensovida/DatosEduardo/DatosEduardoFiltered.csv'

    #Store filtered data
    
    calibracionvalue = 15
    gruposegundos = 5
    senalmaximo = -95
    porcentajeTraining = 0.8
        
    UserMatrixModels = DataFiltered.FilterExecution(calibracionvalue,gruposegundos,senalmaximo,dataFile, pathResult,operation)
    
    if operation == 1:
    
        DataPathTraining = '/home/izubizarreta/Documentos/Documentos/Comercial/Sensovida/DatosEduardo/DatosEduardoTraining.csv'
        DataPathTest = '/home/izubizarreta/Documentos/Documentos/Comercial/Sensovida/DatosEduardo/DatosEduardoTest.csv'
    
        DataFiltered.setStoreTrainingTest(UserMatrixModels, porcentajeTraining, DataPathTraining, DataPathTest)
    
except:
    print ""
    print 'Error filtrando o escribiendo datos'
    print ""