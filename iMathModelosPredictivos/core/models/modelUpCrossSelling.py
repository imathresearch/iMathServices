from iMathModelosPredictivos.core.models.model import Model
from iMathModelosPredictivos.common.util.ioOperations import IOOperations
from iMathModelosPredictivos.common.constants import CONS
from iMathModelosPredictivos.common.util.iMathServicesError import iMathServicesError

from iMathModelosPredictivos.common.util.Postgresl.PostgreslManage import PostgreslManage
from iMathModelosPredictivos.common.util.datesOperations import DateOperations
from iMathModelosPredictivos.common.util.Elasticsearch.ElasticsearchClass import ElasticsearchClass


from scipy import spatial
from operator import itemgetter
import pickle
import numpy as np
import ujson
import collections
import csv

CONS = CONS()

class ModelUpCrossSelling(Model):
    '''
    Extends:
        Class Model from iMathMasMovil.core.model   
    '''
    
    def __init__(self,classifierType=None):

        self.tableData = CONS.TABLE_DATA_NAME_CROSSUP_SELLING
        self.service = CONS.NAME_CROSSUP_SELLING
        self.tableResults = CONS.TABLE_RESULT_NAME_CROSSUP_SELLING
        self.dictionaryName = CONS.INDEX_NAME_CROSSUP_SELLING
        self.tableDataProduct = CONS.TABLE_DATA_PRODUCT_CROSSUP_SELLING
        self.productName = CONS.COLUMN_PRODUCT_NAME_CROSSUP_SELLING
        super(ModelUpCrossSelling, self).__init__(classifierType)
        
    def loadModel(self):
        """Abstract method to be implemented in one of the subclasses
        Args:
          dataFile (string): The file where the model, previously created and saved, resides.        
        """
        try:
            objectData,self.key= self.connectionPostgres.loadModel(self.tableModel,self.service)

        except iMathServicesError as e:
            print "Access Database Error: " , e.value
            return

        else:
           self._serialToModel(self.serialization.getLoads(objectData))
        
    def saveModel(self):

        ModelSerialization = self.serialization.getDumps(self._modelToSerial())
        dates = DateOperations()
        parameters = [self.service,ModelSerialization,0,0,dates.getActualDate()]
        self.key=self.connectionPostgres.setStoreModel(self.tableModel, parameters, self.service)
    

                
    def createModel(self, classifierType):
        """Abstract method to be implemented in one of the subclasses
        Args:
          dataFile (string): The file where the data to create the model resides.
          classifierType (string): String that indicates the type of classifierType to be used to create the model 
              We will probably offer several classifier to create the same model
        """ 
        # Open and read data

        allData = self.connectionPostgres.getDataToCreateModel(self.tableData, self.columnData)
        self.list_sub_bonds = self.getSecuenceProductServices(allData,0)
        
        self.classiferClass = classifierType
        if self.classiferClass == 'Amazon':
            print "[iMathResearch] Creando modelo para up y cross selling basado en 'Amazon collaborative filtering'"
            self._fit()
            self.name = "Amazon collaborative filtering"
        
        print "[iMathResearch] Modelo para up y cross selling creado"  
            
    def _fit(self):
        
        '''This part of the code is necessary to modify for the last function.
        It is necessary to recover data from the database.'''
        
        listProductsServices = self.getDistinctProductService()

        list_cod_bonds = []
        position = 0
        for productService in listProductsServices:
            list_cod_bonds.append(position)
            position = position + 1

        self.bonds_matrix = np.zeros((len(self.list_sub_bonds), len(list_cod_bonds)))

        bond_id = 0
        # bonds_dic is a dictionary which contains for each bond cod, its column index in bonds_matrix
        self.bonds_dic = {} 
        for bond in list_cod_bonds:
            self.bonds_dic[bond] = bond_id
            bond_id += 1

        sub_id = 0
        for sub in self.list_sub_bonds:
            for b in sub:
                self.bonds_matrix[sub_id][self.bonds_dic[b]] = 1
            sub_id += 1
    
    def testModel(self):
        return 0
    
    def predictModel(self):
        """Abstract method to be implemented in one of the subclasses
        Args:
          dataFile (string): The file where the data to be classified resides.
          outputFile (string): String that indicates the complete path of the file where the result of the testing is going to be saved. 
        """
        # Open and read data
        allData = self.connectionPostgres.getAllData(self.tableData, self.columnData,'0')
        self.list_sub_bonds = self.getSecuenceProductServices(allData,1)
        
        print "[iMathResearch] Realizando la prediccion"
        recommendation = self._predict()
                
        '''It will be necessary to store to visualize in the web page of the customer'''
        
        print "[iMathResearch] Prediccion generada"
        
        return  recommendation
        
        
    def _predict(self):
                
        dic_sub_recommended = {}        
        for sub in self.list_sub_bonds:
            #if len(sub) < 2:
            #    raise iMathServicesError("[iMathResearch] Cada fila en el fichero de entrada debe contener al menos dos columnas: ID_SUBSCRIPCION    CODIGO_BONO")
            
            id_sub = 0  # Id de la subscripcion
            # dic_sub_recommended is a dictionary firstly indexed by the subscription id
            # For each subscription, there are two dictionaries:
            #    - current, which contains a list of the bonds associate with the subscription
            #    - recommended, having as target bond the first one, it contains a list of the bonds recommended by the algoritm
            dic_sub_recommended[id_sub] = {}
            bonds = sub
            dic_sub_recommended[id_sub]['current'] = bonds[0:1].tolist()
            #if mode == 'test':
            #    target_bonds = bonds[0:1]

            target_bonds = bonds
            
            # 1. Getting the row in the data matrix model that also buy the bonds specified in target_bonds
            sub_buy_target_bond = np.where(self.bonds_matrix[:, self.bonds_dic[target_bonds[0]]] > 0)[0].tolist()
            for i in range (1, len(target_bonds)):
                aux = np.where(self.bonds_matrix[:, self.bonds_dic[target_bonds[i]]] > 0)[0].tolist()
                sub_buy_target_bond = set(sub_buy_target_bond).intersection(aux)
            
            # 2. Getting the bonds that also have been bought by subscriptions that bought the target bond
            list_bonds = []
            index_target_bonds = []
            for b in target_bonds:
                index_target_bonds.append(self.bonds_dic[b])
            for sub in sub_buy_target_bond:
                bonds_to_compare = np.where(self.bonds_matrix[sub, :] > 0)[0].tolist()
                for b in bonds_to_compare:
                    if b not in index_target_bonds:
                        list_bonds.append(b)
            
            # 3. Calculating the similarity between the target bonds and the list of candidate bonds in list_bonds
            set_bonds = set(list_bonds)
            dic_similarity = {}
            for bond_compare in set_bonds:
                column_bond = self.bonds_matrix[:, bond_compare]
                similarity = 0
                for target_bond in target_bonds:
                    column_target_bond = self.bonds_matrix[:, self.bonds_dic[target_bond]]                                      
                    similarity += 1 - spatial.distance.cosine(column_target_bond, column_bond)
                dic_similarity[bond_compare] = similarity / len(target_bonds)
            
            # 4. Creating a list of tuples where each tuple contains the real cod associated to a bond and the similarity with the target bond
            list_recommended = []
            for bond, similarity in dic_similarity.items():
                for cod_bond, index in self.bonds_dic.items():
                        if bond == index:
                            list_recommended.append((cod_bond, similarity))                   
                            break
            
            # 5. Sorting list_recommended by similarity and returning the 5 bonds more similar to the targer bond
            list_recomendados = sorted(list_recommended, key=itemgetter(1), reverse=True)
            if len(list_recomendados) < 5:        
                dic_sub_recommended[id_sub]['recommended'] = [i[0] for i in list_recomendados]
            else:
                dic_sub_recommended[id_sub]['recommended'] = [i[0] for i in list_recomendados[:5]]
            
        return dic_sub_recommended
        
        
    def _getStatistics(self, recommendations):
        
        percent_hits = {}
        for sub in recommendations:
            hit = 0
            current = recommendations[sub]['current']
            recommended = recommendations[sub]['recommended']
            for i in range(1, len(current)):
                if current[i] in recommended:
                    hit = hit + 1
            if len(current) == 1:
                percent = 100
            else:
                percent = round(int((float(hit) / (len(current) - 1)) * 100), -1)
            
            if percent in percent_hits:
                percent_hits[percent] = percent_hits[percent] + 1
            else:
                percent_hits[percent] = 1 
        
        return collections.OrderedDict(sorted(percent_hits.items(), reverse=True))
    
    def getDistinctProductService(self):
        
        query = 'select distinct(' + str(self.productName) + ') from imathservices."' + self.tableData + '" where "operationData" = ' + "'" + str(0) + "';"
        objectData = np.unique(self.connectionPostgres.getQueryMatrixFormat(query))
        return objectData
    
    def getSecuenceProductServices(self,allData,operation):
        
        query = 'select * from imathservices."' + self.tableDataProduct + '" where "operationData" = ' + "'" + str(operation) + "'" + ';'
        objectData = self.connectionPostgres.getQueryMatrixFormat(query)
        
        codes = np.unique(objectData[:,1])
        listCustomersProductServices = []
        position = 0
        
        for code in codes:
            
            listCustomerProductServices = []
            codesProductServices = np.where(objectData==code)
            for codeProductService in codesProductServices[0]:
                listCustomerProductServices.append(int(objectData[codeProductService,2]))
            listCustomersProductServices.append(listCustomerProductServices)
            position = position + 1
            
        return np.array(listCustomersProductServices)


    def _serialToModel(self,objectSerialized):


        self.bonds_matrix = self.toSave['bonds_matrix']
        self.bonds_dic = self.toSave['bonds_dic']
        self.name = self.toSave['name']


        print "[iMathResearch] Modelo basado en " + self.name + " cargado"


    def _modelToSerial(self):

        objectSerialized = {}
        # Models

        return objectSerialized