'''
Created on Nov 23, 2015

@author: izubizarreta
'''

import tornado.ioloop
import tornado.web

class BestCandidateForEachJobHandler(tornado.web.RequestHandler):
    
    def getParameterValue(self,param):
        
        value = self.get_argument(param)
        return value
    
    def getParameterValues(self,param):
        
        values = self.get_arguments(param)
        return values
    
    def get(self):
        
        value = self.getParameterValue("")      
        
    def post(self):
        
        value = self.getParameterValue("")