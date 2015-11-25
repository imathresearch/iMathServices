'''
Created on Nov 25, 2015

@author: izubizarreta
'''

from time import gmtime, strftime

class DateOperations(object):
    '''
    classdocs
    '''


    def getActualDate(self):
        
        return strftime("%Y-%m-%d %H:%M:%S", gmtime())