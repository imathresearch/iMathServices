'''
Created on 1 de oct. de 2015

@author: izubizarreta
'''

class ConfigurationData(object):
    '''
    classdocs
    '''
     
    def getData(self, data):
        
        file = open(data, 'r')
        
        Codes = []
        
        for line in file:
            
            try:
                position = line.index('=')
            except:
                position = -1
            if position >= 0:
                key = line[:position]
                code = line[position + 1:]
                code = code[:-1]
            
            Codes.append(code)
            
        return Codes
