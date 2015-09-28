from iMathModelosPredictivos.core.modelUpCrossSelling import ModelUpCrossSelling


#dataFile = '/home/andrea/MasMovilIbercom/DataAnalysis/entrega3/analisis_bonos/amazon/subscripcionesPrepago_listabonos_TRAIN.csv'
#m = ModelUpCrossSelling(dataFile,'Amazon')

modelFile = '/home/andrea/MasMovilIbercom/DataAnalysis/modelos/modelo_AmazonUpCross.txt'
m = ModelUpCrossSelling(modelFile)


testFile = '/home/andrea/MasMovilIbercom/DataAnalysis/entrega3/analisis_bonos/amazon/small_test.csv'
outputFile = '/home/andrea/MasMovilIbercom/DataAnalysis/entrega3/analisis_bonos/amazon/prediccion2_test.csv'


#m.testModel(testFile, outputFile)
m.predictModel(testFile, outputFile)