'''
Created on Nov 26, 2015

@author: izubizarreta
'''
from iMathModelosPredictivos.common.constants import CONS

CONS = CONS()
class jsonOperations(object):
    '''
    classdocs
    '''

    def getResultDictChurnCustomer(self,model,code,label,probabiblities):

        dictValue = {"model" : model,
                     "nombre":code[1],
                     "telefono":code[3],
                     "email":code[4],"code" : code[0],
                     "provincia": code[6],
                     "edad":int(code[2]),
                     "codigopostal":code[5],
                     "probabilitiesMembership" : probabiblities,
                     "gastoanual":float(code[24]),
                     "sex":code[7],
                     "geoposicion":CONS.PROVINCES[code[6]]
                     }
        return dictValue

    def getResultDictDownEmployee(self,model,code,label,probabiblities):

        dictValue = {"model" : model,
                     "nombre":code[1],
                     "telefono":code[3],
                     "email":code[4],
                     "code" : code[0],
                     "provincia": code[6],
                     "edad":int(code[2]),
                     "codigopostal":code[5],
                     "probabilitiesMembership" : probabiblities,
                     "sex":code[14],
                     "tiempoempresa":int(code[33]),
                     "viajes":code[7],
                     "dailyrate":int(code[8]),
                     "departamento":code[9],
                     "distanciacasa":int(code[10]),
                     "educacion":code[12],
                     "satisfaccionentorno":int(code[13]),
                     "roltrabajo":code[18],
                     "satisfacciontrabajo":int(code[19]),
                     "sueldo":int(code[21]),

                     }
        return dictValue


    
    def getMatrixToString(self,listProbabilities):
        
        probabilityValues = ''
        for probability in listProbabilities:
            probabilityValues = probabilityValues + str(probability) + ","
                    
        probabilityValues = probabilityValues[:-1]
        return probabilityValues
        
    def getResultsDict(self,model,codes,labels,probabilities,service):
        
        dictValues = []
        probabilitiesPosition = 0
        
        for label in labels:
            if service == 'ChurnCustomer':
                dictValue = self.getResultDictChurnCustomer(model, codes[probabilitiesPosition], label, self.getMatrixToString(probabilities[probabilitiesPosition]))
            elif service == 'DownEmployee':
                dictValue = self.getResultDictDownEmployee(model, codes[probabilitiesPosition], label, self.getMatrixToString(probabilities[probabilitiesPosition]))
            dictValues.append(dictValue)
            probabilitiesPosition+=1
        return dictValues