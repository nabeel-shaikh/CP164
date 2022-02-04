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

from Queue_array import Queue
from Food_utilities import read_foods
from utilities import queue_test

file = open("foods.txt","r")
source = read_foods(file)

queue_test(source)

    