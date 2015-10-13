# (C) 2015 iMath Research S.L. - All rights reserved.
'''
@author: iMath
'''
import os

def constant(f):
    '''
    Decorator to indicate that a property of a class is a constant, so, cannot be set, only get
    '''
    def fset(self, value):
        raise SyntaxError
    def fget(self):
        return f()
    return property(fget, fset)


class CONS(object):
    '''
    It define the global constants    
    '''
    
    @constant
    def MODEL_FILE_LOCATION():
        return "../Data/modelo_"
    
    @constant
    def MODEL_FILE_METADATA_PREDICTUSER():
        return '../Data/metadataPredictPosition.txt' 