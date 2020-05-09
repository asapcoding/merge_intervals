'''
Created on 07.05.2020

@author: asapcoding
'''
'''libraries import / Bibliotheken einbinden '''
from tkinter import filedialog
from openpyxl import Workbook

'''function / Funktion '''
def savefile(newvalues):
    # ask user which save path
    # fragt den Benutzer wo das Ergebnis gespeichert werden soll
    file_path = filedialog.asksaveasfilename(title = "Exceldatei speichern",filetypes = (("excel files","*.xlsx"),))
    
    # if: user choose path, else: if not 
    # if: Benutzer hat Pfad und Name ausgewählt, else: wenn nicht
    if file_path:
        
        # gets workbook and active it
        # holt Arbeitsmappe und aktiviert sie
        book = Workbook()
        ws = book.active
        
        # converts integers to string
        # konvertiert Ganzzahlen in Zeichenfolgen
        valu = newvalues.astype('S')
        
        # converts matrix to list
        # konvertiert Matrix zu Liste
        val = valu.tolist()
        
        # append list to workbook
        # Liste an Arbeitsmappe anhängen
        for row in val:
            ws.append(row)
        
        # saves workbook to the chosen path 
        # speichert die Exceldatei im ausgewählten Pfad
        book.save(file_path)
        
        # returns 1 if the file was saved
        # Gibt 1 zurück, wenn die Datei gespeichert wurde
        return 1
    else:
        # returns 0 if the file was not saved
        # gibt 0 zurück, wenn die Datei nicht gespeichert wurde
        return 0
