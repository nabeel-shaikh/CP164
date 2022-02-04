'''

--------------------------------------------
[CP164 A1]
--------------------------------------------

Author: Nabeel Shaikh
ID: 190741640
Email: shai1640@mylaurier.ca
__updated__ = '2020-10-07'
---------------------------------------------
'''
# Imports
#from Food_utilities import read_foods
#from Queue_circular import Queue
from Food_utilities import read_foods
from Queue_circular import Queue
file = open("foods.txt","r")
source = read_foods(file)
test = Queue()
print("Circular Queue is empty? " + str(test.is_empty()))
print("")

print("Adding 10 food objects to Circular Queue")

for x in range(10):
    test.insert(source[x])

print()
print("Test to see if peak and remove work")
print()
print("Peak of Circular Queue:")
print(test.peek())
print("")
print("Food object is removed from Circular Queue")
print(test.remove())


