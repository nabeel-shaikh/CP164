'''

--------------------------------------------
[CP164 A1]
--------------------------------------------

Author: Nabeel Shaikh
ID: 190741640
Email: shai1640@mylaurier.ca
__updated__: 2020-11-26
---------------------------------------------
'''
# Imports
from BST_linked import BST

x=BST()
x.insert(10)
x.insert(9)
x.insert(8)
x.insert(4)
x.insert(3)
x.insert(11)
print(x.parent_r(11))
print(x.parent(11))
print()
print(x.parent_r(15))
print(x.parent(15))
print()
print(x.parent_r(3))
print(x.parent(3))
