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
from Stack_array import Stack
from functions import stack_split_alt

source = Stack()
source.push(5)
source.push(7)
source.push(8)
source.push(9)
source.push(12)
source.push(14)
source.push(8)

target1, target2 = stack_split_alt(source)

print("Target 1 values")
for x in target1:
    print(x)
    
print("Target 2 values")
for x in target2:
    print(x)
    
