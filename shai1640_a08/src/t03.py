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
from BST_linked import BST
from Letter import Letter
from pip._vendor.html5lib._ihatexml import letter
from functions import letter_table



x = BST()
a=Letter("A")
b=Letter("B")
c=Letter("C")
d=Letter("D")
a==b
b==c
b==a
c==d
x.insert(a)
x.insert(b)
x.insert(c)
x.insert(d)

letter_table(x)


