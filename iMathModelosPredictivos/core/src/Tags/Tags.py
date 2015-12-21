'''
Created on 1 de oct. de 2015

@author: izubizarreta
'''
import random

class Tags(object):
    '''
    classdocs
    '''


    def __init__(self, ListOfTags):
        '''
        Constructor
        '''
        self.ListOfTags = ListOfTags
        
    def getListOfTags(self):
        
        ListOfTags = []
        
        for tags in self.ListOfTags:
            ListOfTags.append(tags)
            
        return ListOfTags
        
    def getTag(self, position):
        
        return self.ListOfTags[position]
        
    def setTag(self, newTag):
        
        self.ListOfTags.append(newTag)
