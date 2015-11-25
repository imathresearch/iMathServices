'''
Created on Nov 25, 2015

@author: izubizarreta
'''
import pickle

class Serialization(object):
    '''
    classdocs
    '''
        
    def getLoads(self,text):
        
        return pickle.loads(text.decode("base64"))
    
    def getDumps(self,object):
        
        return pickle.dumps(object).encode("base64").strip()