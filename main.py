# -*- coding: utf-8 -*-
'''
Created on 07.05.2020

@author: asapcoding
'''

'''libraries import / Bibliotheken einbinden'''
import tkinter as tk

'''link external modules / externe Module einbinden'''
from loadexcelfile import loadfile
from calculate import calculation
from saveexcelfile import savefile

''' defines the main window and the elements / definiert das Hauptfenster und die Elemente'''
class mainframe(tk.Frame):
        def __init__(self, master=None):
            tk.Frame.__init__(self, master)   
            self.grid()
            self.place(x=0, y=0, width=800, height=600)
            
            '''call info elements / ruft die info elemente auf'''
            self.infoframe()
            self.infoheadline()
            self.informationtext()
            self.exampleimage()
            
            '''call calculation elements / ruft die Berechnungselemente auf '''
            self.calculationframe()
            self.calculateheadline()
            self.step1text()
            self.selectbutton()
            self.excelfileinfo()
            self.step2text()
            self.startbutton()
            self.calculationstatus()
            
            '''call save result elements / ruft die Speicherungselemente auf '''
            self.step3text()
            self.savebutton()
            self.savestatus()
            
        '''information frame / Informationen Rahmen '''
        def infoframe(self):
            self.inframe = tk.Frame(self, bd=2, relief='groove')
            self.inframe.grid()
            self.inframe.place(relx=0.01, rely=0.01, width=340, height=446)
            
        '''program information / Programm Information Überschrift '''
        def infoheadline(self):
            self.infotxt = tk.Label(self, text = "Programminformationen",font=('Arial', 12,'bold'), justify='left')
            self.infotxt.grid()
            self.infotxt.place(relx=0.02, rely=0.02)
            
        ''' program information text / Programm Informationen Text '''
        def informationtext(self):
            intext = """Dieses Programm verbindet Intervale die in einer Exceltabelle 
abgelegt sind. Dabei muss folgende Vorgabe eingehalten 
werden. Pro Zeile ein Interval, in Spalte A den Anfangswerte 
der Intervale und in Spalte B die Endwerte.
Das folgende Bild zeigt ein Beispiel:"""
            self.infotxt = tk.Label(self, text = intext, justify='left')
            self.infotxt.grid()
            self.infotxt.place(relx=0.02, rely=0.06)
            
        ''' example image / Beispielbild '''
        def exampleimage(self):
            self.eximg = tk.PhotoImage(file='beispielabbildung.png')
            self.xplimg = tk.Label(self, image=self.eximg)
            self.xplimg.grid()
            self.xplimg.place(relx=0.02, rely=0.20, width=318, height=320)
            
        ''' calculation frame / Berechnung Rahmen '''
        def calculationframe(self):
            self.calframe = tk.Frame(self, bd=2, relief='groove')
            self.calframe.grid()
            self.calframe.place(relx=0.45, rely=0.01, width=340, height=446)
            
        ''' calculation headline / Berechnung Überschrift '''
        def calculateheadline(self):
            self.caltxt = tk.Label(self, text = "Intervale verbinden",font=('Arial', 12,'bold'), justify='left')
            self.caltxt.grid()
            self.caltxt.place(relx=0.47, rely=0.02)
            
        ''' calculation step1 text / Berechnung Schritt 1 Text '''
        def step1text(self):
            self.stp1txt = tk.Label(self, text = "Schritt 1: wählen Sie die Exceldatei aus", justify='left')
            self.stp1txt.grid()
            self.stp1txt.place(relx=0.47, rely=0.06)
            
        ''' select excel table button / wähle Exceltabelle Schaltfläche '''
        def selectbutton(self):
            self.slctbttn = tk.Button(self, text='Exceldatei wählen',font=('Arial', 10), command=self.selectbuttonpushed)
            self.slctbttn.grid()
            self.slctbttn.place(relx=0.47, rely=0.1, width=130, height=26)
        ''' select button pushed / wähle Exceltabelle Schaltfläche wurde gedrückt '''
        def selectbuttonpushed(self):
            # call function to load a excel-file 
            # Funktionsaufruf um die Exceltabelle zu laden
            self.values = loadfile()
            
            if isinstance(self.values, int):
                self.exfileinfo['text'] = "Exceldatei: Datei konnte nicht geladen werden" 
            else:
                self.exfileinfo['text'] = "Exceldatei: Datei wurde geladen" 
                self.strtbttn.config(state="normal")
            
        '''info excel-file is loaded / Informationsfeld über Zustand des Ladevorgangs '''
        def excelfileinfo(self):
            self.exfileinfo = tk.Label(self, text='Exceldatei: keine Datei ausgewählt')
            self.exfileinfo.grid()
            self.exfileinfo.place(relx=0.47, rely=0.15)
            
        ''' calculation step2 text / Berechnung Schritt 2 Text '''
        def step2text(self):
            self.stp2txt = tk.Label(self, text = "Schritt 2: Starten Sie die Berechnung", justify='left')
            self.stp2txt.grid()
            self.stp2txt.place(relx=0.47, rely=0.2)
            
        ''' calculation start-button / Berechnung Start Schaltfläche '''
        def startbutton(self):
            self.strtbttn = tk.Button(self, text='starten',font=('Arial', 10), state='disabled', command=self.startbuttonpushed)
            self.strtbttn.grid()
            self.strtbttn.place(relx=0.47, rely=0.25, width=130, height=26)
            
        ''' calculation start button pushed / Berechnung Start Schaltfläche wurde gedrückt '''
        def startbuttonpushed(self):
            self.slctbttn.config(state="disabled")
            self.strtbttn.config(state="disabled")
            self.calstat['text'] = "Status: wird berechnet" 
            self.savestat['text'] = "Status: nicht gespeichert" 
            # call function to calculate the values
            # Funktionsaufruf zur Berechnung der Werte
            self.newvalues = calculation(self.values)
            
            self.calstat['text'] = "Status: Berechnung abgeschlossen!" 
            self.strtbttn.config(state="normal")
            self.slctbttn.config(state="normal")
            self.savebttn.config(state="normal")
            
        ''' calculation status / Status Berechnung '''
        def calculationstatus(self):
            self.calstat = tk.Label(self, text='Status: wählen Sie zuerst die Datei aus')
            self.calstat.grid()
            self.calstat.place(relx=0.47, rely=0.30)
        
        ''' save step3 text / Speichern Schritt 3 Text '''
        def step3text(self):
            self.stp3txt = tk.Label(self, text = "Schritt 3: Ergebnis in einer Exceldatei speichern", justify='left')
            self.stp3txt.grid()
            self.stp3txt.place(relx=0.47, rely=0.35)
            
        ''' save button / Speichern Schaltfläche '''
        def savebutton(self):
            self.savebttn = tk.Button(self, text='speichern',font=('Arial', 10), state='disabled', command=self.savebuttonpushed)
            self.savebttn.grid()
            self.savebttn.place(relx=0.47, rely=0.40, width=130, height=26)
            
        ''' save button pushed / Speichern Schaltfläche wurde gedrückt'''
        def savebuttonpushed(self):
            self.slctbttn.config(state="disabled")
            self.strtbttn.config(state="disabled")
            self.savebttn.config(state="disabled")
            # call function to save the results in a excel-file
            # Funktionsaufruf zur Speicherung des Ergebnisses in einer neuen Exceltabelle
            stat = savefile(self.newvalues)
            
            self.slctbttn.config(state="normal")
            self.strtbttn.config(state="normal")
            self.savebttn.config(state="normal")
            if stat == 1:
                self.savestat['text'] = "Status: Datei wurde gespeichert!" 
            else:
                self.savestat['text'] = "Status: Datei konnte nicht gespeichert!" 
                
        ''' save status / Speichern Status'''
        def savestatus(self):
            self.savestat = tk.Label(self, text='Status: nicht gespeichert')
            self.savestat.grid()
            self.savestat.place(relx=0.47, rely=0.45)
            
            
''' call main window / Aufruf Hauptfenster'''
app = mainframe()
app.master.title('Intervalle verbinden')
app.master.geometry('708x460')

app.mainloop()  
