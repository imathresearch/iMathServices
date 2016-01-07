import os
import iMathModelosPredictivos as module
from os.path import expanduser


def constant(f):
    '''
    Decorator to indicate that a property of a class is a constant, so, cannot be set, only get
    '''
    def fset(self, value):
        raise SyntaxError
    def fget(self):
        return f()
    return property(fget, fset)


class CONS_PRODUCT(object):

    @constant
    def FIELD_PRODUCT_ID():
        return 'product_id'

    @constant
    def FIELD_GROUP_PRODUCT_ID():
        return 'group_product_id'

    @constant
    def FIELD_PRODUCT_NAME():
        return 'product_name'

    @constant
    def FIELD_PRODUCT_PRICE():
        return 'product_price'

    @constant
    def FIELD_PRODUCT_IMAGE_PATH():
        return 'product_image_path'