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
from functions import insert_words, comparison_total
from Hash_Set_sorted import Hash_Set

hash_set = Hash_Set(7)
fv=open("miserables.txt","r")
insert_words(fv, hash_set)
total,max_word = comparison_total(hash_set)

print("Using array-based Sorted List Hash_Set")
print()
print("Total Comparisons: " + str(total))
print("Word with maximum comparisons {}".format(max_word))
