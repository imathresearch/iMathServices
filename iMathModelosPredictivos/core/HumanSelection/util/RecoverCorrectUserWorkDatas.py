'''
Created on 6 de oct. de 2015

@author: izubizarreta
'''

'''It will be necessary to convert this algorithm dynamic. Now, it is totally static.'''

def getUserCriteriasValues(user):
    
    id = user[0]
    edad = user[1]
    works = [user[2], user[4], user[6], user[8], user[10]]
    yearsworks = [user[3], user[5], user[7], user[9], user[11]]
    degree = [user[12]]
    yearsdegree = [user[13]]
    languages = [user[14], user[16], user[18], user[20]]
    yearslanguages = [user[15], user[17], user[19], user[21]]
    
    Tags = []
    for value in range(22, len(user) - 1):
        Tags.append(user[value])
        
    return [id, edad, works, yearsworks, degree, yearsdegree, languages, yearslanguages, Tags]

def getWorkCriteriasValues(WorkList):
    
    id = WorkList[0]
    edad = WorkList[1]
    works = [WorkList[2]]
    yearsworks = [WorkList[3]]
    degree = [WorkList[4]]
    yearsdegree = [WorkList[5]]
    languages = [WorkList[6], WorkList[8], WorkList[10], WorkList[12]]
    yearslanguages = [WorkList[7], WorkList[9], WorkList[11], WorkList[13]]
    
    Tags = []
    for value in range(14, len(WorkList) - 1):
        Tags.append(WorkList[value])
        
    return [id, edad, works, yearsworks, degree, yearsdegree, languages, yearslanguages, Tags]
