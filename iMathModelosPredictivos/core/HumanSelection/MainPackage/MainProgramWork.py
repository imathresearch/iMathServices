'''
Created on 1 de oct. de 2015

@author: izubizarreta
'''

import random

from iMathModelosPredictivos.core.HumanSelection.Works.Work import Work
import numpy as np
from iMathModelosPredictivos.core.HumanSelection.util import ConvertDataToMatrix

pathFileWriteWorkResults = '../Data/randomWork.csv'

WorkQuantity = range(1)
TypeJobs = range(100)
TypeDegrees = range(100)
TagsQuantity = range(20)
LanguageQuantities = range(0, 4)
MaximumNumberOfWorkingYearsMenus25 = 4
MaximumNumberOfWorkingYearsMenus40 = 7
MaximumNumberOfWorkingYearsMenus65 = 10

WorkData = []

for userquantity in WorkQuantity:
    
    edad = random.randint(18, 65)
    
    worksList = [random.randint(1, 100)]
    
    if ((edad >= 20) & (edad <= 25)): 
        yearsList = [random.randint(1, MaximumNumberOfWorkingYearsMenus25)]
    else:
        if ((edad >= 25) & (edad <= 40)):
            yearsList = [random.randint(1, MaximumNumberOfWorkingYearsMenus40)]
        else:
            yearsList = [random.randint(1, MaximumNumberOfWorkingYearsMenus65)]
                
    titulosList = [random.randint(1, len(TypeDegrees))]
    titulosYear = [1]

    LanguageValues = []
    YearsLanguages = []    
    
    for language in LanguageQuantities:
        ItHave = random.randint(0, 1)
        if ItHave == 1:
            LanguageValues.append(ItHave)
            YearsLanguages.append(random.randint(1, 5))
        else:
            LanguageValues.append(0)
            YearsLanguages.append(0)
            
    Tags = []
    
    for tags in TagsQuantity:
        ItHaveTag = random.randint(0, 1)
        if ItHaveTag == 1:
            Tags.append(ItHaveTag)
        else:
            Tags.append(0)
            
    newWork = Work(random.randint(1, 9999999999), edad, worksList, yearsList, titulosList, titulosYear, LanguageValues, YearsLanguages, Tags)

    WorkData.append(newWork)
    
WorkDataMatrix = ConvertDataToMatrix.getMatrixUser(WorkData)

WorkDataMatrix = np.array(WorkDataMatrix)

np.savetxt(pathFileWriteWorkResults, WorkDataMatrix, fmt='%s', delimiter=',')
