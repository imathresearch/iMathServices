'''
Created on 6 de oct. de 2015

@author: izubizarreta
'''

class Criterias(object):
    '''
    classdocs
    '''


    def __init__(self, number,priority):
        '''
        Constructor
        '''
        self.parameters = self.setCriterias(number, priority)
        self.percentageValueEachCriteria = self.setPercentageCriteriasValue()
        
    def setCriterias(self,number,priority):
        list_priorities = []
        for char in priority:
            list_priorities.append(float(char))

        parameters=[]
        parameters.append(['NumberOfElements', float(number), []])
        parameters.append(['PriorityLevel', '', list_priorities])
        parameters.append(['MaximumDifference', 5.0, []])
        return parameters
        '''
        fileOpen = open(path,'r')
        parameters = []
        
        for row in fileOpen:
            parameter = []
            positionEqual = row.index('=')
            key = row[0:positionEqual]
            value = row[positionEqual+1:]
            try:
                positionCommas = value.index(',')
            except:
                positionCommas = -1
            elementsComma = []
            if positionCommas>-1:
                rangeCommas = range(len(value[:-1]))
                for commavalue in rangeCommas:                    
                    if value[commavalue]!=',':
                        elementsComma.append(float(value[commavalue]))
            parameter.append(key)
            if positionCommas==-1:
                if len(value)>1:
                    parameter.append(float(value[:-1]))
                else:
                    parameter.append(float(value))
            else:
                parameter.append(value)
            parameter.append(elementsComma)
            parameters.append(parameter)
            
        return parameters
        '''

    def getCriteriaValues(self):
        
        return self.parameters
    
    def getCriteriaKeyValue(self,param):
        
        parameters = self.parameters
        parameter = 0
        
        for parameter in parameters:
            if (parameter[0] == param):
                return parameter
            
        return parameter
    
    def getMatchingPercentageValues(self):
        
        keyValueParameters = self.getCriteriaKeyValue('PriorityLevel')
        return keyValueParameters[2]
    
    def getNumberOfElements(self):
        
        keyValueParameters = self.getCriteriaKeyValue('NumberOfElements')
        return keyValueParameters[1]
    
    def getMaximumDiffereneValue(self):
        
        keyValueParameters = self.getCriteriaKeyValue('MaximumDifference')
        return keyValueParameters[1]
    
    def setPercentageCriteriasValue(self):
        
        CriteriasValues = self.getMatchingPercentageValues()
        IntervalValues = []
        position = 0
        TotalCriterias = 0
        
        for criteria in CriteriasValues:
            IntervalValues.append(1 / criteria)
            TotalCriterias = TotalCriterias + IntervalValues[position]
            position = position + 1
            
        position = 0
        for interval in IntervalValues:
            IntervalValues[position] = interval / TotalCriterias
            position = position + 1
            
        return IntervalValues
    
    def getPercentageCriteriasValue(self):
        
        return self.percentageValueEachCriteria