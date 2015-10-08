'''
Created on 1 de oct. de 2015

@author: izubizarreta
'''

import random

from iMathModelosPredictivos.core.HumanSelection.Users.User import User
import numpy as np
from iMathModelosPredictivos.core.HumanSelection.util import ConvertDataToMatrix

pathFileWriteWorkResults = '../Data/randomUsers.csv'

UserQuantity = range(100)
TypeJobs = range(100)
TypeDegrees = range(100)
TagsQuantity = range(20)
LanguageQuantities = range(0, 4)
MaximumNumberOfWorkingYearsMenus25 = 4
MaximumNumberOfWorkingYearsMenus40 = 7
MaximumNumberOfWorkingYearsMenus65 = 10

UsersData = []

for userquantity in UserQuantity:
    
    edad = random.randint(18, 65)
    
    if ((edad >= 20) & (edad <= 25)):                
        works = range(2)
        worksList = [random.randint(1, 100), random.randint(1, 100), 0, 0, 0]
        lengthList = len(works)
        years = edad - 20
        if works != 1:
            yearsList = [float(random.randint(1, MaximumNumberOfWorkingYearsMenus25)), float(random.randint(1, MaximumNumberOfWorkingYearsMenus25)), 0, 0, 0]
    else:
        if ((edad >= 25) & (edad <= 40)):
            works = range(4)
            worksList = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), 0]
            lengthList = len(works)
            years = edad - 20
            if works != 1:
                yearsList = []
                for worksl in works:
                    yearsList.append(float(random.randint(1, MaximumNumberOfWorkingYearsMenus40)))
                yearsList.append(0)
        else:
            works = range(5)
            worksList = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]
            lengthList = len(works)
            years = edad - 20
            if works != 1:
                yearsList = []
                for worksl in works:
                    yearsList.append(float(random.randint(1, MaximumNumberOfWorkingYearsMenus65)))
                
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
            
    newUser = User(random.randint(1, 9999999999), edad, worksList, yearsList, titulosList, titulosYear, LanguageValues, YearsLanguages, Tags)

    UsersData.append(newUser)
    
UserDataMatrix = ConvertDataToMatrix.getMatrixUser(UsersData)

UserDataMatrix = np.array(UserDataMatrix)

np.savetxt(pathFileWriteWorkResults, UserDataMatrix, fmt='%s', delimiter=',')
