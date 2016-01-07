# (C) 2015 iMath Research S.L. - All rights reserved.
'''
@author: iMath
'''
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


class CONS(object):
    '''
    It define the global constants for the iMathMasMovil core
    
    '''
    @constant
    def MODEL_FILE_LOCATION():
        home = expanduser("~")
        return os.path.join(home, "modelos_predictivos/modelo_")
    
    @constant
    def MODEL_FILE_METADATA():
        path = os.path.dirname(module.__file__)
        return os.path.join(path, 'data', 'metadataUserModel.txt') 
    
    @constant
    def MODEL_UPCROSS_LIST_BONOS():
        path = os.path.dirname(module.__file__)
        return os.path.join(path, 'data', 'list_codbonos.csv')
    
    @constant
    def MODEL_FILE_METADATA_NEWCUSTOMER():
        path = os.path.dirname(module.__file__)
        return os.path.join(path, 'data', 'metadataNewCustomerModel.txt') 

    @constant
    def MODEL_FILE_METADATA_DOWNCUSTOMER():
        path = os.path.dirname(module.__file__)
        return os.path.join(path, 'data', 'metadataDownCustomer.txt')
    
    @constant
    def MODEL_FILE_METADATA_DOWNEMPLOYEE():
        path = os.path.dirname(module.__file__)
        return os.path.join(path, 'data/BBDDHeaders', 'metadataDownEmployee.txt')

    @constant
    def MODEL_FILE_METADATA_GOCUSTOMER():
        path = os.path.dirname(module.__file__)
        return os.path.join(path, 'data', 'metadataGoCustomer.txt')
    
    @constant
    def MODEL_FILE_METADATA_GOCUSTOMER_BBDD():
        path = os.path.dirname(module.__file__)
        path = path + '/data/BBDDHeaders/metadataGoCustomer.txt'
        path = str(path)
        return path

    @constant
    def MODEL_FILE_METADATA_TRANSPORT():
        path = os.path.dirname(module.__file__)
        return os.path.join(path, 'data/Transport', 'metadataUserModelTransport.txt') 
    
    @constant
    def MODEL_UPCROSS_LIST_BONOS_TRANSPORT():
        path = os.path.dirname(module.__file__)
        return os.path.join(path, 'data/Transport', 'list_codbonos.csv')
    
    @constant
    def MODEL_FILE_METADATA_NEWCUSTOMER_TRANSPORT():
        path = os.path.dirname(module.__file__)
        return os.path.join(path, 'data/Transport', 'metadataNewCustomerModel.txt') 

    @constant
    def MODEL_FILE_METADATA_DOWNCUSTOMER_TRANSPORT():
        path = os.path.dirname(module.__file__)
        return os.path.join(path, 'data/Transport', 'metadataDownCustomer.txt') 

    @constant
    def MODEL_FILE_METADATA_GOCUSTOMER_TRANSPORT():
        path = os.path.dirname(module.__file__)
        return os.path.join(path, 'data/Transport', 'metadataGoCustomer.txt') 

    @constant
    def MODEL_FILE_METADATA_BANKING():
        path = os.path.dirname(module.__file__)
        return os.path.join(path, 'data/Banking', 'metadataUserModelTransport.txt') 
    
    @constant
    def MODEL_UPCROSS_LIST_BONOS_BANKING():
        path = os.path.dirname(module.__file__)
        return os.path.join(path, 'data/Banking', 'list_codbonos.csv')
    
    @constant
    def MODEL_FILE_METADATA_NEWCUSTOMER_BANKING():
        path = os.path.dirname(module.__file__)
        return os.path.join(path, 'data/Banking', 'metadataNewCustomerModel.txt') 

    @constant
    def MODEL_FILE_METADATA_DOWNCUSTOMER_BANKING():
        path = os.path.dirname(module.__file__)
        return os.path.join(path, 'data/Banking', 'metadataDownCustomer.txt') 

    @constant
    def MODEL_FILE_METADATA_GOCUSTOMER_BANKING():
        path = os.path.dirname(module.__file__)
        return os.path.join(path, 'data/Banking', 'metadataGoCustomer.txt') 


    '''
        TWITTER
    
        It will be necessary to create a new twitter user to recover data.
        Necessary Data: Consumer_key, Consumer_secrt, Access_Toke,, Access_Token_Secret
    '''

    @constant
    def CONSUMER_KEY():
        return 'NIPqiUBMkGgEPsZTUGvWzIAGv'
    
    @constant
    def CONSUMER_SECRET():
        return '6Qb6eX8c6lOg7Vuh1ageW92ucddylC7unytJ3crJTBYgdVARcW'
    
    @constant
    def ACCESS_TOKEN():
        return '519460742-P9llilYNcuy1VUtuASOnHOFhJStJyuiD75M18mEZ'
    
    @constant
    def ACCESS_TOKEN_SECRET():
        return '8jGzEMsrkuT5nvuxnmp8Zcpt9WM6Xdxm3F3OCpUafLMw8'
    
    @constant
    def TWITTER_DB():
        return "test_db"
    
    @constant
    def TOKEN_LAST_TWEET():
        return 'LAST_ELEMENT'
    
    @constant
    def STOPWORDS_FILE():
        return '../data/stopwords.txt'




    '''
        It define the global constants to connect to the elasticsearch database

    '''
    @constant
    def HOST_ELASTICSEARCH():
        return 'localhost'

    @constant
    def PORT_ELASTICSEARCH():
        return 9200

    @constant
    def PROVINCES():
        return  {            "Alava":"42.9099989,-2.6983868",
                             "Albacete":"38,99765,-1,86007",
                             "Alicante":"38.3459963,-0.4906855",
                             "Almeria":"36.834047,-2.4637136",
                             "Avila":"40.656685,-4.6812086",
                             "Badajoz":"38.8794495,-6.9706535",
                             "Baleares":"39.5341789,2.8577105",
                             "Barcelona":"41.3850639,2.1734035",
                             "Burgos":"42.3439925,-3.696906",
                             "Caceres":"39.4752765,-6.3724247",
                             "Cadiz":"36.5270612,-6.2885962",
                             "Castellon":"39.9863563,-0.0513246",
                             "Ciudad Real":"38.9848295,-3.9273778",
                             "Cordoba":"37.8881751,-4.7793835",
                             "Coruna":"43.3623436,-8.4115401",
                             "Cuenca":"40.0703925,-2.1374162",
                             "Girona":"41.9794005,2.8214264",
                             "Granada":"37.1773363,-3.5985571",
                             "Guadalajara":"40.632489,-3.16017",
                             "Gipuzkoa":"43.0756299,-2.2236667",
                             "Huelva":"37.261421,-6.9447224",
                             "Huesca":"42.131845,-0.4078058",
                             "Jaen":"37.7795941,-3.7849057",
                             "Leon":"42.5987263,-5.5670959",
                             "Lleida":"41.6175899,0.6200146",
                             "La Rioja":"42.2870733,-2.539603",
                             "Lugo":"43.0097384,-7.5567582",
                             "Madrid":"40.4167754,-3.7037902",
                             "Malaga":"36.721261,-4.4212655",
                             "Murcia":"37.9922399,-1.1306544",
                             "Navarra":"42.6953909,-1.6760691",
                             "Ourense":"42.3357893,-7.863881",
                             "Asturias":"43.3613953,-5.8593267",
                             "Palencia":"42.0096857,-4.5288016",
                             "Las Palmas":"28.1235459,-15.4362574",
                             "Pontevedra":"42.4298846,-8.6446202",
                             "Salamanca":"40.9701039,-5.6635397",
                             "Tenerife":"28.2915637,-16.6291304",
                             "Cantabria":"43.1828396,-3.9878427",
                             "Segovia":"40.9429032,-4.1088069",
                             "Sevilla":"37.3890924,-5.9844589",
                             "Soria":"41.7665972,-2.4790306",
                             "Tarragona":"41.1188827,1.2444909",
                             "Teruel":"40.3456879,-1.1064345",
                             "Toledo":"39.8628316,-4.0273231",
                             "Valencia":"39.4699075,-0.3762881",
                             "Valladolid":"41.652251,-4.7245321",
                             "Bizkaia":"43.2204286,-2.6983868",
                             "Zamora":"41.5034712,-5.7467879",
                             "Zaragoza":"41.6488226,-0.8890853",
                             "Ceuta":"35.8893874,-5.3213455",
                             "Melilla":"35.2922775,-2.9380973"
                        }

    @constant
    def INDEX_NAME_CHURN_CUSTOMER():
        return "telcoresults"

    @constant
    def PROPERTIES_INDEX_ELASTIC_CHURN_CUSTOMER():
        return {
                "settings" : {
                        "number_of_shards": 1,
                        "number_of_replicas": 0
                },
                "mappings" : {
                        "blog" : {
                            "_source" : { "enabled" : False },
                            "properties" :{

                                    "code":                     { "type" : "string",  "index" : "analyzed", "analyzer" : "keyword"},
                                    "codigopostal":             { "type" : "string",  "index" : "analyzed", "analyzer" : "keyword"},
                                    "edad":                     { "type" : "integer",  "index" : "analyzed"},
                                    "provincia":                { "type" : "string",  "index" : "analyzed","analyzer" : "keyword"},
                                    "email":                    { "type" : "string",  "index" : "analyzed","analyzer" : "keyword"},
                                    "gastoanual":               { "type" : "float",  "index" : "analyzed"},
                                    "model":                    { "type":"string","index" : "analyzed", "analyzer" : "keyword"},
                                    "nombre":                   { "type":"string","index" : "analyzed", "analyzer" : "keyword"},
                                    "probabilitiesMembership":  { "type" : "string",  "index" : "analyzed", "analyzer" : "keyword"},
                                    "sex":                      { "type":"string","index" : "analyzed"},
                                    "telefono":                 { "type" : "string",  "index" : "analyzed", "analyzer" : "keyword"},
                                    "geoposicion":              {"type": "geo_point"}
                                    }
                        }
                }
            }


    @constant
    def INDEX_NAME_DOWN_EMPLOYEE():
        return "downemployeeresults"

    @constant
    def PROPERTIES_INDEX_ELASTIC_DOWN_EMPLOYEE():
        return {
                "settings" : {
                        "number_of_shards": 1,
                        "number_of_replicas": 0
                },
                "mappings" : {
                        "blog" : {
                            "_source" : { "enabled" : False },
                            "properties" :{

                                    "code":                     { "type" : "string",  "index" : "analyzed", "analyzer" : "keyword"},
                                    "codigopostal":             { "type" : "string",  "index" : "analyzed", "analyzer" : "keyword"},
                                    "edad":                     { "type" : "integer",  "index" : "analyzed"},
                                    "provincia":                { "type" : "string",  "index" : "analyzed","analyzer" : "keyword"},
                                    "email":                    { "type" : "string",  "index" : "analyzed","analyzer" : "keyword"},
                                    "tiempoempresa":            { "type" : "integer",  "index" : "analyzed"},
                                    "model":                    { "type":"string","index" : "analyzed", "analyzer" : "keyword"},
                                    "nombre":                   { "type":"string","index" : "analyzed", "analyzer" : "keyword"},
                                    "probabilitiesMembership":  { "type" : "string",  "index" : "analyzed", "analyzer" : "keyword"},
                                    "sex":                      { "type":"string","index" : "analyzed"},
                                    "telefono":                 { "type" : "string",  "index" : "analyzed", "analyzer" : "keyword"},
                                    "viajes":                   { "type" : "string",  "index" : "analyzed","analyzer" : "keyword"},
                                    "dailyrate":                { "type" : "integer",  "index" : "analyzed"},
                                    "departamento":             { "type" : "string",  "index" : "analyzed","analyzer" : "keyword"},
                                    "distanciacasa":            { "type" : "integer",  "index" : "analyzed"},
                                    "educacion":                { "type" : "string",  "index" : "analyzed","analyzer" : "keyword"},
                                    "satisfaccionentorno":      { "type" : "integer",  "index" : "analyzed"},
                                    "roltrabajo":               { "type" : "string",  "index" : "analyzed","analyzer" : "keyword"},
                                    "satisfacciontrabajo":      { "type" : "integer",  "index" : "analyzed"},
                                    "sueldo":                   { "type" : "integer",  "index" : "analyzed"}

                                    }
                        }
                }
            }

    @constant
    def INDEX_NAME_CROSSUP_SELLING():
        return "crossupselling_results"




    '''
        It define the global constants to connect to the postgresql database

    '''
    @constant
    def HOST_POSTGRESQL():
        return 'localhost'

    @constant
    def USER_POSTGRESQL():
        return 'antonio'
    @constant
    def PASSWORD_POSTGRESQL():
        return '1234'

    @constant
    def DATABASE_POSTGRESQL():
        return 'imathservices'

    @constant
    def TABLE_MODEL_POSTGRESQL():
        return 'Model'



    '''
            Name of each model

    '''
    @constant
    def NAME_CHURN_CUSTOMER():
        return 'ChurnCustomer'

    @constant
    def NAME_DOWN_EMPLOYEE():
        return 'DownEmployee'

    @constant
    def NAME_CROSSUP_SELLING():
        return 'CrossUpSelling'




    '''
            GoCustomer constants in Postgres

    '''
    @constant
    def TABLE_DATA_NAME_CHURN_CUSTOMER():
        return 'CompleteData'

    @constant
    def TABLE_RESULT_NAME_CHURN_CUSTOMER():
        return 'resultsModel'


    '''
            DownEmployee constants in Postgres

    '''
    @constant
    def TABLE_DATA_NAME_DOWN_EMPLOYEE():
        return 'CompleteDataDownEmployee'

    @constant
    def TABLE_RESULT_NAME_DOWN_EMPLOYEE():
        return 'resultsModel'

    '''
            CrossUpSelling constants in Postgres

    '''
    @constant
    def TABLE_DATA_NAME_CROSSUP_SELLING():
        return 'PurchaseData'

    @constant
    def TABLE_RESULT_NAME_CROSSUP_SELLING():
        return 'resultsModel'

    @constant
    def TABLE_DATA_PRODUCT_CROSSUP_SELLING():
        return 'ProductsCustomer'

    @constant
    def COLUMN_PRODUCT_NAME_CROSSUP_SELLING():
        return 'productname'




    '''
        It define the constants to work with datasheets
    '''

    @constant
    def COLUMN_CLASS_DATASHEETS():
        return 'operationData'

    '''
        Commons Tables database postgres constants
    '''

    @constant
    def TABLE_PRODUCTS():
        return 'Products'

    @constant
    def TABLE_SERVICES():
        return 'Services'
