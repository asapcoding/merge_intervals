# merge_intervals
The program combines overlapping intervals.
The user can load an Excel spreadsheet with intervals through a simple user interface.
Then the program connects all intervals from the Excel table that overlap.
The result can then be saved to a new Excel spreadsheet.

## restriction
The intervals must be closed and integers, for example [2,10]. 
The table may only be described in columns A and B. 
The first interval must be in the first line and no text. 
One interval per line. cell A < B applies in one row.
Only Excel files with the extension .xlsx can be loaded.

What is the maximum possible value of an integer in Python ?
Source: https://www.geeksforgeeks.org/what-is-maximum-possible-value-of-an-integer-in-python/

The range of values is limited, but the number of values depends on the available memory.
Eclipse IDE: Self tested:  OverflowError: Python int too large to convert to C long
http://openbook.rheinwerk-verlag.de/c_von_a_bis_z/005_c_basisdatentypen_004.htm

# modules discription
### main.py
* contains the GUI part
* calls all other modules
### loadexcelfile.py
* opens dialog box to choose the .xlsx-file
* excludes files that do not meet the requirements
* returns a matrix with the values from the table
### calculate.py
* the interval with the smallest value in column A is focused in each loop pass
* intervals that overlap with the focused interval are searched for
* the focused interval and the found intervals are deleted from the matrix and written as a connected interval in a new matrix
* the new matrix is returned
### saveexcelfile.py
* gets the new matrix
* opens a dialog box to save the new matrix as a .xlsx-file

# Intervalle verbinden
Das Programm kombiniert überlappende Intervalle. Der Benutzer kann eine Excel-Tabelle mit Intervallen über eine einfache Benutzeroberfläche laden. Anschließend verbindet das Programm alle Intervalle aus der Excel-Tabelle, die sich überschneiden. Das Ergebnis kann dann in einer neuen Excel-Tabelle gespeichert werden.

## Beschränkung
Die Intervalle müssen geschlossen und ganzzahlig sein, zum Beispiel [2,10]. Die Tabelle darf nur in den Spalten A und B beschrieben werden. In der ersten Zeile darf kein Text stehen. Ein Intervall pro Zeile. Es gilt Zelle A? < B? in einer Zeile. Es können nur Excel-Dateien mit der Endung .xlsx geladen werden.

Was ist der maximal mögliche Wert einer Ganzzahl in Python?
Quelle: https://www.geeksforgeeks.org/what-is-maximum-possible-value-of-an-integer-in-python/

Der Wertebereich ist eingeschränkt jedoch richtet sich die Anzahl der Werte nach dem verfügbaren Speicher.
Eclipse IDE: selbst getestet:  OverflowError: Python int too large to convert to C long
http://openbook.rheinwerk-verlag.de/c_von_a_bis_z/005_c_basisdatentypen_004.htm

# Modulbeschreibung
### main.py
* enthält den GUI-Teil
* ruft alle anderen Module auf

### loadexcelfile.py
* öffnet ein Dialogfeld zur Auswahl der XLSX-Datei
* schließt Dateien aus, die die Anforderungen nicht erfüllen
* gibt eine Matrix mit den Werten aus der Tabelle zurück

### calculate.py
* das Intervall mit dem kleinsten Wert in Spalte A wird in jedem Schleifendurchgang fokussiert
* es wird nach Intervallen gesucht, die sich mit dem fokussierten Intervall überschneiden
* das fokussierte Intervall und die gefundenen Intervalle werden aus der Matrix gelöscht und als verbundenes Intervall in eine neue Matrix geschrieben
* die neue Matrix wird zurückgegeben

### saveexcelfile.py
* übernimmt die neue Matrix
* öffnet ein Dialogfeld zum Speichern der neuen Matrix als XLSX-Datei
