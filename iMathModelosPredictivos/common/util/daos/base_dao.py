import psycopg2
import abc
from iMathModelosPredictivos.common.constants import CONS
CONS = CONS()


class BaseDAO(object):

    def __init__(self):

        self.db = psycopg2.connect("host=" +CONS.HOST_POSTGRESQL + " " +
                                   "user=" +CONS.USER_POSTGRESQL + " " +
                                   "password=" +CONS.PASSWORD_POSTGRESQL+ " "+
                                   "dbname=" + CONS.DATABASE_POSTGRESQL)






    def closeConnection(self):

        self.db.close()
        return 0