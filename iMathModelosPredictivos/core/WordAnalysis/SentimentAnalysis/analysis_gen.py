# (C) 2014 iMath Research S.L. - All rights reserved.
""" The abstract class that implements the access to a classifier for sentiment analysis

Authors:

@author iMath
"""

import abc

class SentimentAnalysis(object):
    
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def __init__(self):
        pass
    
    @abc.abstractmethod  
    def predict(self, data):
        pass
    
    def updateModel(self, data):
        pass