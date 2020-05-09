'''
Created on 07.05.2020

@author: asapcoding
'''
'''libraries import'''
import numpy as np

'''functions'''
def calculation(values):

    # splits the matrix into two array of column A and column B 
    intvalA = values[:,0] # begin of the intervals
    intvalB = values[:,1] # end of the intervals
    
    # defines the arrays for the new intervals
    newvaluesA = np.array([],dtype=int)
    newvaluesB = np.array([],dtype=int)
    
    # one interval is focused in each loop pass
    # while: until the specified interval array is empty
    while len(intvalA) > 0:
        
        # it starts with the interval that has the smallest values and gets the row index of it 
        min_value_idxA = np.argmin(intvalA)
        
        # the interval under consideration will be stored in its own variables
        currentA = intvalA[min_value_idxA]
        currentB = intvalB[min_value_idxA]
        
        # the interval under consideration is deleted in the values-array
        intvalA = np.delete(intvalA, min_value_idxA)
        intvalB = np.delete(intvalB, min_value_idxA)
        
        # search intervals in intvalA in range of the interval that has the smallest value
        intvalsinrangeAidx = np.where((intvalA >= currentA) & (intvalA <=currentB))[0]
        
        # gets the values in intvalB of intervals in range
        intvalinrangeB = intvalB[intvalsinrangeAidx, ]
        
        # deletes the intervals in range of the interval under consideration
        intvalA = np.delete(intvalA, intvalsinrangeAidx)
        intvalB = np.delete(intvalB, intvalsinrangeAidx)
        
        # if variable intvalinrangeB is empty take the last value of the interval under consideration
        if np.any(intvalinrangeB) == False:
            endofnewintval = currentB
        else:
            # gets the index of the max value in intvalinrangB
            endofnewintval = np.amax(intvalinrangeB)
        
        # saves the found values in an array
        newvaluesA = np.append(newvaluesA, currentA);
        newvaluesB = np.append(newvaluesB, endofnewintval);
        
    # glues the new arrays together
    newvalues = np.stack((newvaluesA,newvaluesB),axis=-1)

    # return the matrix with the new intervals
    return newvalues