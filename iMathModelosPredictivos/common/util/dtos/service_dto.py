class ServiceDTO(object):

    def __init__(self,service_id, group_service_id, service_name, service_price, service_image_path):

        self._service_id= service_id
        self._group_service_id = group_service_id
        self._service_name = service_name
        self._service_price = service_price
        self._service_image_path = service_image_path



##DC:==========================================================================
##DC: GETTERS
##DC:==========================================================================

    @property
    def service_id(self):
        return self._service_id

    @property
    def group_service_id(self):
        return self._group_service_id

    @property
    def service_name(self):
        return self._service_name

    @property
    def service_price(self):
        return self._service_price

    @property
    def service_image_path(self):
        return self._service_image_path



##DC:==========================================================================
##DC: SETTERS
##DC:==========================================================================

    @service_id.setter
    def service_id(self, service_id):
        self._service_id = service_id

    @group_service_id.setter
    def group_service_id(self, group_service_id):
        self._group_service_id = group_service_id

    @service_name.setter
    def service_name(self, service_name):
        self._service_name = service_name

    @service_price.setter
    def service_price(self, service_price):
        self._service_price = service_price

    @service_image_path.setter
    def service_image_path(self, service_image_path):
        self._service_image_path = service_image_path

