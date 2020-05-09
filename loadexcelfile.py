'''
Created on 07.05.2020

@author: asapcoding
'''
'''libraries import'''
from openpyxl import load_workbook
from tkinter import filedialog
import numpy as np

'''functions'''
def loadfile():
    # opens dialog box to choose the excel-file
    file_path = filedialog.askopenfilename(title = "Exceldatei laden",filetypes = (("excel files","*.xlsx"),))
    
    # if: user selects a excel-file else: the user cancel the dialog box
    if file_path:
        # loads the excel-file into memory
        workbook = load_workbook(filename=file_path, data_only=True)
    
        # gets first sheet of excel-table
        sheet = workbook.active

        # gets the dimension of the sheet
        sheetdim = sheet.dimensions
    
        # checks that the first cell is A1
        if sheetdim[0:2] == 'A1':
            
            # searches for B to ensure that the table has the given size
            posB = sheetdim.find('B')
            
            # checks that the second column is B
            if  posB != -1:
                
                # splits the string into single character to get the number of letters
                dimSplit = list(sheetdim)
                
                # gets the number of letters
                dimEnd = len(dimSplit)
                
                # gets the number after B, join the character to one number
                lengthcol = int(''.join(dimSplit[posB+1:dimEnd]))

                # creates a matrix 2 x length of column
                dataAB = np.zeros((lengthcol,2),dtype=int)
                
                # fill up the matrix with the value from excel-table
                for x in range(1,lengthcol+1): 
                    
                    # gets values
                    dA = sheet.cell(row = x,column = 1)
                    dB = sheet.cell(row = x,column = 2)
                    
                    # write values into matrix
                    dataAB[x-1,0] = dA.value
                    dataAB[x-1,1] = dB.value
                    
                # return the matrix
                return dataAB
            else:
                # return 0 to flag an error
                return 0
        else:
            # return 0 to flag an error
            return 0
    else:
        # return 0 to flag an error
        return 0