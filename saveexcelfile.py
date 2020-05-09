'''
Created on 07.05.2020

@author: asapcoding
'''
'''libraries import'''
from tkinter import filedialog
from openpyxl import Workbook

'''functions'''
def savefile(newvalues):
    # ask user which save path
    file_path = filedialog.asksaveasfilename(title = "Exceldatei speichern",filetypes = (("excel files","*.xlsx"),))
    
    # if user choose path, else if not 
    if file_path:
        
        # get workbook and active it
        book = Workbook()
        ws = book.active
        
        # convert integers to string
        valu = newvalues.astype('S')
        
        # convert matrix to list
        val = valu.tolist()
        
        # append list to workbook
        for row in val:
            ws.append(row)
        
        # saves workbook to the chosen path 
        book.save(file_path)
        
        # returns 1 if the file was saved
        return 1
    else:
        # returns 0 if the file was not saved
        return 0