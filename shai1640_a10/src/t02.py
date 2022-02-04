'''

--------------------------------------------
[CP164 A1]
--------------------------------------------

Author: Nabeel Shaikh
ID: 190741640
Email: shai1640@mylaurier.ca
__updated__: 2020-12-03
---------------------------------------------
'''
# Imports
from Sorts_List_linked import Sorts
from List_linked import List
a=List()
a.append(1)
a.append(5)
a.append(4)
a.append(6)
a.append(2)
Sorts.radix_sort(a)
for x in a:
    print(x)

print()
a=List()
a.append(11)
a.append(5)
a.append(43)
a.append(66)
a.append(21)
Sorts.radix_sort(a)
for x in a:
    print(x)

