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
from functions import do_comparisons
from functions import comparison_total
from Letter import Letter

DATA1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

bst = BST()
bst2 = BST()
bst3 = BST()

for x in DATA1:
    bst.insert(Letter(x))
    
for x in DATA2:
    bst2.insert(Letter(x))

for x in DATA3:
    bst3.insert(Letter(x))


file_variable = open("miserables.txt","r")

do_comparisons(file_variable, bst)
do_comparisons(file_variable, bst2)
do_comparisons(file_variable, bst3)

file_variable.close()

total=comparison_total(bst)
total2=comparison_total(bst2)
total3=comparison_total(bst3)

print("Comparing by order: " + DATA1)
print("Total Comparisons: {}".format(total))
print('------------------------------------------------------------')
print("Comparing by order: " + DATA2)
print("Total Comparisons: {}".format(total2))
print('------------------------------------------------------------')
print("Comparing by order: " + DATA3)
print("Total Comparisons: {}".format(total3))






