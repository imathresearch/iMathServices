import psycopg2


class SingletonType(type):

    def __call__(cls, *args, **kwargs):
        try:
            return cls.__instance

        except AttributeError:

            cls.__instance = super(SingletonType, cls).__call__(*args, **kwargs)
            return cls.__instance


class ConnectionManager(object):

    __metaclass__ = SingletonType

    def __init__(self, host, user, password, database):
        pass
        #self.db = psycopg2.connect(connectstring)



if __name__ == "__main__":
    pass



