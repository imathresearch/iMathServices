'''
Created on Nov 26, 2015

@author: izubizarreta
'''

class jsonOperations(object):
    '''
    classdocs
    '''

    def getResultDict(self,model,code,label,probabiblities):
        
        dictValue = {"model" : model, "nombre":code[1],"telefono":code[3],"email":code[4],"code" : code[0], "label" : label, "probabilitiesMembership" : probabiblities}
        return dictValue
    
    def getMatrixToString(self,listProbabilities):
        
        probabilityValues = ''
        for probability in listProbabilities:
            probabilityValues = probabilityValues + str(probability) + ","
                    
        probabilityValues = probabilityValues[:-1]
        return probabilityValues
        
    def getResultsDict(self,model,codes,labels,probabilities):
        
        dictValues = []
        probabilitiesPosition = 0
        
        for label in labels:
            
            dictValue = self.getResultDict(model, codes[probabilitiesPosition], label, self.getMatrixToString(probabilities[probabilitiesPosition]))
            dictValues.append(dictValue)
            probabilitiesPosition+=1
        return dictValues