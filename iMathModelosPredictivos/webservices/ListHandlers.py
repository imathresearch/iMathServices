'''
Created on Nov 23, 2015

@author: izubizarreta
'''
import tornado.ioloop
import tornado.web

from iMathModelosPredictivos.webservices.handlers.churnCustomerHandlers import ChurnCustomerHandler
from iMathModelosPredictivos.webservices.handlers.downEmployeeHandler import DownEmployeeHandler
from iMathModelosPredictivos.webservices.handlers.selectCandidatesHandler import SelectBestCandidatesHandler
from iMathModelosPredictivos.webservices.handlers.crossUpSellingHandlers import CrossUpSellingHandler
from iMathModelosPredictivos.webservices.handlers.retentionCustomerHandler import RetentionCustomerHandler
class ListHandlers(object):
    '''
    classdocs
    '''

    def make_app(self):

        return tornado.web.Application([
                                        (r"/ChurnCustomer", ChurnCustomerHandler),
                                        (r"/DownEmployee", DownEmployeeHandler),
                                        (r"/BestCandidates", SelectBestCandidatesHandler),
                                        (r"/CrossSelling", CrossUpSellingHandler),
                                        (r"/RetentionCustomer", RetentionCustomerHandler),
                                        ])

    def createListApplications(self, ListPath, HandlerList):

        return 0
