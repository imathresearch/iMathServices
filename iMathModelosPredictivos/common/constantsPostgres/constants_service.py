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


class CONS_SERVICE(object):

    @constant
    def FIELD_SERVICE_ID():
        return 'service_id'

    @constant
    def FIELD_GROUP_SERVICE_ID():
        return 'group_service_id'

    @constant
    def FIELD_SERVICE_NAME():
        return 'service_name'

    @constant
    def FIELD_SERVICE_PRICE():
        return 'service_price'

    @constant
    def FIELD_SERVICE_IMAGE_PATH():
        return 'service_image_path'