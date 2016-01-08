class ProductDTO(object):

    def __init__(self,product_id, group_product_id, product_name, product_price, product_image_path):

        self._product_id= product_id
        self._group_product_id = group_product_id
        self._product_name = product_name
        self._product_price = product_price
        self._product_image_path = product_image_path



##DC:==========================================================================
##DC: GETTERS
##DC:==========================================================================

    @property
    def product_id(self):
        return self._product_id

    @property
    def group_product_id(self):
        return self._group_product_id

    @property
    def product_name(self):
        return self._product_name

    @property
    def product_price(self):
        return self._product_price

    @property
    def product_image_path(self):
        return self._product_image_path



##DC:==========================================================================
##DC: SETTERS
##DC:==========================================================================

    @product_id.setter
    def product_id(self, product_id):
        self._product_id = product_id

    @group_product_id.setter
    def group_product_id(self, group_product_id):
        self._group_product_id = group_product_id

    @product_name.setter
    def product_name(self, product_name):
        self._product_name = product_name

    @product_price.setter
    def product_price(self, product_price):
        self._product_price = product_price

    @product_image_path.setter
    def product_image_path(self, product_image_path):
        self._product_image_path = product_image_path

