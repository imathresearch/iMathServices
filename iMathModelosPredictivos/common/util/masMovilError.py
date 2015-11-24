'''
Created on 02/02/2015

@author: andrea
'''
class MasMovilError(Exception):
     def __init__(self, value):
         self.value = value
     def __str__(self):
         return repr(self.value)
