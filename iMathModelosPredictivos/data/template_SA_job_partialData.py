import os
from iMathModelosPredictivos.core.WordAnalysis.Twitter.TwitterTracking.twitterTrack import TwitterTracker
from iMathModelosPredictivos.core.WordAnalysis.SentimentAnalysis.analysisNB import NbAnalyzer
import json

'''
l_query = [<<QUERY>>]
timeout = <<TIME>>
fileName_partialData = '<<FILE>>'
'''

l_query = 0
timeout = 0
fileName_partialData = '0'

tt = TwitterTracker(l_query, timeout, fileName_partialData)
