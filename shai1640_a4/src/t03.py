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
from Priority_Queue_array import Priority_Queue
source = Priority_Queue()
source.insert(1)
source.insert(2)
source.insert(3)
source.insert(4)
source.insert(5)
source.insert(6)
source.insert(7)
target1, target2 = source.split_key(4)

print("Target 2 values")
for x in target2:
    print(x)
