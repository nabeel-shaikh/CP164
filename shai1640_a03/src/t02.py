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


source = Stack()
source.push(1)
source.push(2)
source.push(3)
source.push(4)
source.push(5)
source.push(6)
source.push(7)

target1, target2 = source.split_alt()

print("Target 1 values")
for x in target1:
    print(x)
    
print("Target 2 values")
for x in target2:
    print(x)
    