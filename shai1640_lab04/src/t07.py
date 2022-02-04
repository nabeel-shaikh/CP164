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
from utilities import list_test

file = open("foods.txt","r")
source = read_foods(file)
list_test(source)
file.close()

