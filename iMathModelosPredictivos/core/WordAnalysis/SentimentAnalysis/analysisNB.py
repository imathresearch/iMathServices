# (C) 2014 iMath Research S.L. - All rights reserved.
""" 
    Class that implements a NaiveBayes Analyzer using TextBlob.
    This NaiveBayes Analyzer is provided already trained using a
    corpus of movies reviews
    TextBlob library is designed for processing textual data
Authors:

@author iMath
"""
from textblob import Blobber
from textblob.sentiments import NaiveBayesAnalyzer
from SentimentAnalysis.core.kernel.analysis_gen import SentimentAnalysis


class NbAnalyzer (SentimentAnalysis):
    
    def __init__(self):
        '''
            Create a Blobber object with a NaiveBayesAnalyzer trained with a corpus of 
            movies reviews
        '''
        self.blob = Blobber(analyzer=NaiveBayesAnalyzer())
        
    def predict(self, data):
        ''' 
            Predict/analyse the sentiment of the data parameter.
            data must be a list of tweets (in text).
            Return the sentiment prediction for each tweet in data.
            The sentiment prediction per tweet is a number in [0,1]. 
            0 = Negative ---[range of sentiment]--- Positive = 1 
        '''
        mp = map(self.blob, data)
        return [ t.sentiment[1] for t in mp ]    
        