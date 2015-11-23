'''
Created on Nov 23, 2015

@author: izubizarreta
'''
import tornado.ioloop
import tornado.web
from iMathModelosPredictivos.WebServices.Handlers.MainHandlers import MainHandler
from iMathModelosPredictivos.WebServices.Handlers.BestCandidateForEachJobHandlers import BestCandidateForEachJobHandler
from iMathModelosPredictivos.WebServices.Handlers.ChurnCustomerHandlers import ChurnCustomerHandler
from iMathModelosPredictivos.WebServices.Handlers.ChurnEmployeeHandlers import ChurnEmployeeHandler 

class ListHandlers(object):
    '''
    classdocs
    '''

    def make_app(self):
        
        return tornado.web.Application([
                                        (r"/", MainHandler),
                                        (r"/ChurnCustomer", ChurnCustomerHandler),
                                        (r"/ChurnEmployee", ChurnEmployeeHandler),
                                        (r"/BestCandidateForEachJob", BestCandidateForEachJobHandler),
                                        ])
        
    def createListApplications(self,ListPath,HandlerList):
        
        return 0