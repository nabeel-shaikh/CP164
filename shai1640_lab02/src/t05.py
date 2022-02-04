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
from utilities import stack_test
from Food_utilities import read_foods

file = open("foods.txt","r")

source1 = read_foods(file)
stack_test(source1)

