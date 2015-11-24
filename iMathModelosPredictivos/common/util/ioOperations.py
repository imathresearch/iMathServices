import pickle
import numpy as np
import csv

class IOOperations:
	
	def saveObj2File(self, obj, filePath):
		pickle.dump(obj, filePath);
		
	def loadFile2Obj(self, filePath):
		return pickle.load(filePath);

	def openFile(self, filePath, mode):
		fileDesc = open(filePath, mode)
		return fileDesc
		
	def readTrainDataModelFile(self, fileDesc):
		reader = csv.reader(fileDesc, delimiter='\t')
		rownum = 0
		inputs = []
		output = []
		for row in reader:
			if rownum > 0:
				inputRow = row[0:-1]
				outputRow = row[-1]				
				inputRow = [np.nan if x == '' else x for x in inputRow]
				inputs = inputs + [inputRow]	    
				output = output + [map(int, outputRow)]
			else:
				header = row;
		
			rownum += 1
		
		X = np.vstack(inputs)
		Y = np.vstack(output)
		
		return [header, X, Y]
	
	def readTrainDataModelFileFloat(self, fileDesc):
		
		data = np.genfromtxt(fileDesc, dtype="|S50", delimiter=',', invalid_raise=False)		
		header = data[0, :]		
		X = data[1:, :-1]		
		Y = data[1:, -1:]
		return [header, X, Y]	
	
	def readTrainDataModelFileAbandonoTerminacion(self, fileDesc):

		data = np.genfromtxt(fileDesc, dtype="|S50", delimiter=',', invalid_raise=False)		
		header = data[0, :]		
		X = data[1:, :-1]		
		Y = data[1:, -1:]
		return [header, X, Y]
	
	def readTestDataModelFile(self, fileDesc):
		reader = csv.reader(fileDesc, delimiter='\t')
		rownum = 0
		inputs = []
		for row in reader:
			if rownum > 0:
				inputRow = row
				inputRow = [np.nan if x == '' else x for x in inputRow]
				inputs = inputs + [inputRow]
			else:
				header = row;
		
			rownum += 1
		
		X = np.vstack(inputs)
				
		return [header, X]
	
	def readTestDataModelFileFloat(self, fileDesc):
		
		data = np.genfromtxt(fileDesc, dtype="|S50", delimiter=',', invalid_raise=False)		
		header = data[0, :]		
		X = data[1:, :-1]		
		Y = data[1:, -1:]
		return [header, X, Y]
	
	def readPredictDataModelFileFloat(self, fileDesc):
		
		data = np.genfromtxt(fileDesc, dtype="|S50", delimiter=',', invalid_raise=False)		
		header = data[0, :]		
		X = data[1:, :]		
		return [header, X]
			
	def closeFile(self, fileDesc):
		fileDesc.close()
		return 0
	
	
