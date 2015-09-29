# (C) 2015 iMath Research S.L. - All rights reserved.
'''
@author: iMath
'''
import os
import iMathModelosPredictivos as module
from os.path import expanduser


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
    It define the global constants for the iMathMasMovil core
    
    '''
    @constant
    def MODEL_FILE_LOCATION():
        home = expanduser("~")
        return os.path.join(home, "modelos_predictivos/modelo_")
    
    @constant
    def MODEL_FILE_METADATA():
        path = os.path.dirname(module.__file__)
        return os.path.join(path, 'data', 'metadataUserModel.txt') 
    
    @constant
    def MODEL_UPCROSS_LIST_BONOS():
        path = os.path.dirname(module.__file__)
        return os.path.join(path, 'data', 'list_codbonos.csv')
    
    @constant
    def MODEL_FILE_METADATA_NEWCUSTOMER():
        path = os.path.dirname(module.__file__)
        return os.path.join(path, 'data', 'metadataNewCustomerModel.txt') 

    @constant
    def MODEL_FILE_METADATA_DOWNCUSTOMER():
        path = os.path.dirname(module.__file__)
        return os.path.join(path, 'data', 'metadataDownCustomer.txt') 

    @constant
    def MODEL_FILE_METADATA_GOCUSTOMER():
        path = os.path.dirname(module.__file__)
        return os.path.join(path, 'data', 'metadataGoCustomer.txt') 

    '''
        It will be necessary to create a new twitter user to recover data.
        Necessary Data: Consumer_key, Consumer_secrt, Access_Toke,, Access_Token_Secret
    '''

    @constant
    def CONSUMER_KEY():
        return 'NIPqiUBMkGgEPsZTUGvWzIAGv'
    
    @constant
    def CONSUMER_SECRET():
        return '6Qb6eX8c6lOg7Vuh1ageW92ucddylC7unytJ3crJTBYgdVARcW'
    
    @constant
    def ACCESS_TOKEN():
        return '519460742-P9llilYNcuy1VUtuASOnHOFhJStJyuiD75M18mEZ'
    
    @constant
    def ACCESS_TOKEN_SECRET():
        return '8jGzEMsrkuT5nvuxnmp8Zcpt9WM6Xdxm3F3OCpUafLMw8'
    
    @constant
    def TWITTER_DB():
        return "test_db"
    
    @constant
    def TOKEN_LAST_TWEET():
        return 'LAST_ELEMENT'
    
    @constant
    def STOPWORDS_FILE():
        return '../data/stopwords.txt'
    