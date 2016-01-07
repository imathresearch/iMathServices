import psycopg2
from iMathModelosPredictivos.common.constants import CONS
from iMathModelosPredictivos.common.constantsPostgres.constants_product import CONS_PRODUCT
from iMathModelosPredictivos.common.util.daos.singleton_type import SingletonType
from iMathModelosPredictivos.common.util.daos.base_dao import BaseDAO
from iMathModelosPredictivos.common.util.dtos.product_dto import ProductDTO
CONS = CONS()
CONS_PRODUCT = CONS_PRODUCT()



class ProductDAO(BaseDAO):

    __metaclass__ = SingletonType

    def __init__(self):

        super(ProductDAO, self).__init__()


    def get_all_products(self):

        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM imathservices."' + CONS.TABLE_PRODUCTS + '";')
        results = cursor.fetchall()
        list_dto_products = [self._register_to_dto(product) for product in results]
        return list_dto_products


    def get_product_by_id(self,product_id):
        pass


    def _register_to_dto(self,product):

        return ProductDTO(product[0],
                          product[1],
                          product[2],
                          product[3],
                          product[4])




    def _productdto_to_dict(self,product_dto):
        return  {
            CONS_PRODUCT.FIELD_PRODUCT_ID: product_dto.product_id,
            CONS_PRODUCT.FIELD_GROUP_PRODUCT_ID: product_dto.group_product_id,
            CONS_PRODUCT.FIELD_PRODUCT_NAME: product_dto.product_name,
            CONS_PRODUCT.FIELD_PRODUCT_PRICE: product_dto.product_price,
            CONS_PRODUCT.FIELD_PRODUCT_IMAGE_PATH: product_dto.product_image_path,
        }


if __name__ == "__main__":

    productDAO = ProductDAO()
    products= productDAO.get_all_products()
    list=[productDAO._productdto_to_dict(product) for product in products]
    print list[0:3]





