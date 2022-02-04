'''

--------------------------------------------
[CP164 A1]
--------------------------------------------

Author: Nabeel Shaikh
ID: 190741640
Email: shai1640@mylaurier.ca
---------------------------------------------
'''
# Imports
from Food_utilities import read_foods

file = open("foods.txt", "r")
x = read_foods(file)
file.close()
for y in x:
    print(y)
