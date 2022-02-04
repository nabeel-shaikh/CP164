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
from functions import pq_split_alt

source = Priority_Queue()
source.insert(1)
source.insert(2)
source.insert(3)
source.insert(4)
source.insert(5)
source.insert(6)
source.insert(7)

target1, target2 = pq_split_alt(source)
print("Target 1 values")
for x in target1:
    print(x)