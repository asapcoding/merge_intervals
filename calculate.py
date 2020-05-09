'''
Created on 07.05.2020

@author: asapcoding
'''
'''libraries import / Bibliotheken einbinden'''
import numpy as np

'''function / Funktion '''
def calculation(values):

    # splits the matrix into two array of column A and column B 
    # teilt die Matrix in zwei Arrays von Spalte A und Spalte B auf
    intvalA = values[:,0] # begin of the intervals
    intvalB = values[:,1] # end of the intervals
    
    # defines the arrays for the new intervals
    # definiert die Arrays für die neuen Intervalle
    newvaluesA = np.array([],dtype=int)
    newvaluesB = np.array([],dtype=int)
    
    # one interval is focused in each loop pass
    # while: until the specified interval array is empty
    # ein Intervall wird in jedem Schleifendurchgang fokussiert
    # while: bis das angegebene Intervallarray leer ist
    while len(intvalA) > 0:
        
        # it starts with the interval that has the smallest values and gets the row index of it 
        # es beginnt mit dem Intervall mit den kleinsten Wert in Spalte A und erhält den Zeilenindex
        min_value_idxA = np.argmin(intvalA)
        
        # the interval under consideration will be stored in its own variables
        # Das betrachtete Intervall wird in eigenen Variablen gespeichert
        currentA = intvalA[min_value_idxA]
        currentB = intvalB[min_value_idxA]
        
        # the interval under consideration is deleted in the values-array
        # Das betrachtete Intervall wird im Werte-Array gelöscht
        intvalA = np.delete(intvalA, min_value_idxA)
        intvalB = np.delete(intvalB, min_value_idxA)
        
        # search intervals in intvalA in range of the interval that has the smallest value
        # sucht Interval unter IntvalA im Bereich des betrachteten Intervals
        intvalsinrangeAidx = np.where((intvalA >= currentA) & (intvalA <=currentB))[0]
        
        # gets the values in intvalB of intervals in range
        # erhält die Werte der gefundenen Intervalle
        intvalinrangeB = intvalB[intvalsinrangeAidx, ]
        
        # deletes the intervals in range of the interval under consideration
        # löscht die Intervalle im Bereich des betrachteten Intervalls aus dem Array
        intvalA = np.delete(intvalA, intvalsinrangeAidx)
        intvalB = np.delete(intvalB, intvalsinrangeAidx)
        
        # if variable intvalinrangeB is empty take the last value of the interval under consideration
        # wenn keine Werte im Bereich des betrachteten Intervals gefunden wurden übergib das betrachtete Interval
        if np.any(intvalinrangeB) == False:
            endofnewintval = currentB
        else:
            # gets the index of the max value in intvalinrangB
            # ruft den Index des Maximalwerts in intvalinrangB ab
            endofnewintval = np.amax(intvalinrangeB)
        
        # saves the found values in an array
        # speichert die gefundenen Werte in einem neuen Array
        newvaluesA = np.append(newvaluesA, currentA);
        newvaluesB = np.append(newvaluesB, endofnewintval);
        
    # glues the new arrays together
    # verbindet die neuen array zu einer matrix 2xn
    newvalues = np.stack((newvaluesA,newvaluesB),axis=-1)

    # return the matrix with the new intervals
    # gibt die Matrix mit den neuen Intervallen zurück
    return newvalues
