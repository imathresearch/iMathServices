from iMathModelosPredictivos.common.util.Postgresl.PostgreslManage import PostgreslManage
from iMathModelosPredictivos.common.util.daos.product_dao import ProductDAO
from iMathModelosPredictivos.common.util.daos.service_dao import ServiceDAO
from iMathModelosPredictivos.common.constants import CONS
import random
CONS = CONS()

class ModelRetentionCustomer(object):

    def __init__(self):

        self.product_dao = ProductDAO()
        self.service_dao = ServiceDAO()

    def make_recommendation(self, customer_id):

        result = {}
        productDAO = ProductDAO()
        products= productDAO.get_all_products()
        list_products=[productDAO._productdto_to_dict(product) for product in products]
        random.shuffle(list_products)
        result['products']=list_products[0:2]

        serviceDAO = ServiceDAO()
        services= serviceDAO.get_all_services()
        list_services=[serviceDAO._servicedto_to_dict(service) for service in services]
        random.shuffle(list_services)
        result['services']=list_services[0:1]
        return result