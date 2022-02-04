'''

--------------------------------------------
[CP164 A1]
--------------------------------------------

Author: Nabeel Shaikh
ID: 190741640
Email: shai1640@mylaurier.ca
__updated__: 2020-11-19
---------------------------------------------
'''
# Imports
from BST_linked import BST

x=BST()
x.insert(1)
x.insert(2)
x.insert(0)



print(x.is_balanced())
print(x.is_valid())

y=BST()
y.insert(1)
y.insert(2)
y.insert(0)

print(x.is_identical(y))
print(x.min())
print(y.leaf_count())
print(y.one_child_count())
print(y.two_child_count())
print(x.inorder())
print(x.preorder())
print(x.postorder())
print(x.levelorder())
