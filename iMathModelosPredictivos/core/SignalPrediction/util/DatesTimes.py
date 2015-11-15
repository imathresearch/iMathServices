'''
Created on 1 de oct. de 2015

@author: izubizarreta
'''
from datetime import datetime
import time

class DatesTimes(object):
    '''
    classdocs
    '''

    def __init__(self, datestring):
        '''
        Constructor
        '''
        self.actualDate = datestring
        
    def getDateFormat(self):
        
        StringBecameDateObject = datetime.strptime(self.actualDate, '%Y-%m-%d %H:%M:%S')        
        return StringBecameDateObject
    
    def getTypeTyple(self, value):
        
        return value.timetuple()
    
    def getTime(self, value):
        
        value = self.getTypeTyple(value)
        return time.mktime(value)
