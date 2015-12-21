'''
Created on 6 de oct. de 2015

@author: izubizarreta
'''

'''It will be necessary to convert this algorithm dynamic. Now, it is totally static.'''

def getUserCriteriasValues(user):
    
    id = user[0]
    edad = user[1]
    works = [user[2], user[4], user[6]]
    yearsworks = [user[3], user[5], user[7]]
    degree = [user[8]]
    yearsdegree = [1]
    languages = [user[9], user[11], user[13], user[15]]
    yearslanguages = [user[10], user[12], user[14], user[16]]
    
    Tags = []
    for value in range(17, len(user) - 1):
        Tags.append(user[value])
        
    return [id,edad,works,yearsworks,degree,yearsdegree,languages,yearslanguages,Tags]

def getWorkCriteriasValues(WorkList):
    
    id = WorkList[0]
    edad = WorkList[1]
    works = [WorkList[2]]
    yearsworks = [WorkList[3]]
    degree = [1]
    yearsdegree = [WorkList[4]]
    languages = [WorkList[5]]
    yearslanguages = [WorkList[6]]
    Tags = [WorkList[7]]
        
    return [id,edad,works,yearsworks,degree,yearsdegree,languages,yearslanguages,Tags]