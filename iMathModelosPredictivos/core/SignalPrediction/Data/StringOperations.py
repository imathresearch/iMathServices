'''
Created on 1 de oct. de 2015

@author: izubizarreta
'''
import code

class StringOperations(object):
    '''
    classdocs
    '''

    def getFirstPart(self, string, position):
        key = string[:position]
        return key        
        
    def getLastPart(self, string, position):
        code = string[position + 1:]
        return code
    
    def removeReturnCharacter(self, string):
        string = string[:-1]
        
    def getPositionMatrix(self, Matrix, Value):
        try:
            position = Matrix.index(Value)
            return position
        except:
            position = -1
