'''
Created on 4 de oct. de 2015

@author: izubizarreta
'''

'''Matching Algorithm Calculation'''

from iMathModelosPredictivos.core.HumanSelection.Users.User import User
from iMathModelosPredictivos.core.HumanSelection.Works.Work import Work
from iMathModelosPredictivos.core.HumanSelection.MatchingAlgorithm.MatchingAlgorithm import MatchingAlgorithm
import numpy as np
from iMathModelosPredictivos.core.HumanSelection.util import MatchingAlgorithmCalculationCriterias as matching

def MatchingAlgorithmCalculationProcess(user, work, differenceAges, eachCriteriasPercentage):
    
    '''This function will calculate the mathematical function.
    1.- Cross all the users.
    2.- Verifies the following restrictions:
        2.1- Age - It will be possible to calculate the interval (need +- years) = + 1, (need +- years*2) + 0.5 else 0 
        2.2- Works and years - The same work adds 1 and add the proportion of years calculating the number of years depending the work needs. The percentage desviation is not calculated yet.
        2.3.- Languages and years (0 or 1). Lenguages yes (1) and years (proportion X/5). This proportion will be
    added to the final result.  The percentage desviation, proportion, is not calculated yet.
        2.4.- Tags. If each tag is equal, the algorithm adds 1.
        For each user's criteria, the algorithm multiplier each criteria with its percentage value'''
    
    FinalPoint = 0
    
    Interval = matching.getMatchingUserInterval(user, work, differenceAges)
    IntervalHalf = 0
    if Interval == 0:
        IntervalHalf = matching.getMatchingUserHalfInterval(user, work, differenceAges)
    JobMatchingValue = matching.getJobMatching(user, work)
    DegreeMatchingValue = matching.getDegreeMatching(user, work)
    LanguageMatchingValue = matching.getLanguagesMatching(user, work)
    TagsMatchingValue = 0
    
    # If the user has not got the useful job and degree, it is logic that it has not got any tag.
    
    if ((JobMatchingValue > 0) | (DegreeMatchingValue > 0)):
        TagsMatchingValue = matching.getTagsMatching(user, work)
       
    FinalPoint = FinalPoint + ((Interval + IntervalHalf) * eachCriteriasPercentage[0]) + (JobMatchingValue * eachCriteriasPercentage[1]) + (DegreeMatchingValue * eachCriteriasPercentage[2]) + (LanguageMatchingValue * eachCriteriasPercentage[3]) + (TagsMatchingValue * eachCriteriasPercentage[4])
    
    return FinalPoint 

def generaMatchingAlgorithm(ListOfUsers, work, differenceAges, eachCriteriasPercentage):
    
    ListOfCalculusMatchingValues = []
    
    for user in ListOfUsers:   
        calculusMatching = MatchingAlgorithmCalculationProcess(user, work, differenceAges, eachCriteriasPercentage)
        ListOfCalculusMatchingValues.append(calculusMatching)
        
    return ListOfCalculusMatchingValues

def selectBestNElements(MatchingAlgorithmList, NElements, UserList):
    
    '''Sort and select the first N elements. The first code sorted and the second one gives the sorted
    index. It will be necessary both, but the most import will be the index, because we would like to
    recover the users, or candidates, code.'''   
    
    MatchingAlgorithmListIndex = np.argsort(MatchingAlgorithmList, axis=0)
    rangeNElements = range(int(NElements))
    selectedElements = []
    for rangeValue in rangeNElements:
        position = len(MatchingAlgorithmList) - rangeValue - 1
        selectedElements.append(UserList[MatchingAlgorithmListIndex[position]])
    return selectedElements
