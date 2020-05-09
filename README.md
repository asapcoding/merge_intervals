# merge_intervals
The program combines overlapping intervals.
The user can load an Excel spreadsheet with intervals through a simple user interface.
Then the program connects all intervals from the Excel table that overlap.
The result can then be saved to a new Excel spreadsheet.

## restriction
The intervals must be closed and integers, for example [2,10]. 
The table may only be described in columns A and B. 
The first interval must be in the first line and no text. 
One interval per line. A < B applies.
Only Excel files with the extension .xlsx can be loaded.

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
