import psycopg2
from iMathModelosPredictivos.common.constants import CONS
from iMathModelosPredictivos.common.constantsPostgres.constants_service import CONS_SERVICE
from iMathModelosPredictivos.common.util.daos.singleton_type import SingletonType
from iMathModelosPredictivos.common.util.daos.base_dao import BaseDAO
from iMathModelosPredictivos.common.util.dtos.service_dto import ServiceDTO
CONS = CONS()
CONS_SERVICE = CONS_SERVICE()



class ServiceDAO(BaseDAO):

    __metaclass__ = SingletonType

    def __init__(self):

        super(ServiceDAO, self).__init__()


    def get_all_services(self):

        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM imathservices."' + CONS.TABLE_SERVICES + '";')
        results = cursor.fetchall()
        list_dto_services = [self.register_to_dto(service) for service in results]
        return list_dto_services


    def register_to_dto(self,service):

        return ServiceDTO(service[0],
                          service[1],
                          service[2],
                          service[3],
                          service[4])

    def _servicedto_to_dict(self,service_dto):

        dict=  {
            CONS_SERVICE.FIELD_SERVICE_ID: service_dto.service_id,
            CONS_SERVICE.FIELD_GROUP_SERVICE_ID: service_dto.group_service_id,
            CONS_SERVICE.FIELD_SERVICE_NAME: service_dto.service_name,
            CONS_SERVICE.FIELD_SERVICE_PRICE: service_dto.service_price,
            CONS_SERVICE.FIELD_SERVICE_IMAGE_PATH: service_dto.service_image_path,
    }
        return dict
if __name__ == "__main__":

    serviceDAO = ServiceDAO()
    services= serviceDAO.get_all_services()
    print services
