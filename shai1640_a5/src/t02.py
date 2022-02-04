'''

--------------------------------------------
[CP164 A1]
--------------------------------------------

Author: Nabeel Shaikh
ID: 190741640
Email: shai1640@mylaurier.ca
__updated__ = '2020-10-28'
---------------------------------------------
'''
# Imports
from Sorted_List_array import Sorted_List
from Food_utilities import read_foods

file = open("foods.txt","r")
source = read_foods(file)
target1 = Sorted_List()
target2 = Sorted_List()


for x in range(0,5,1):
    target1.insert(source[x])
    
for x in range(2,7,1):
    target2.insert(source[x])

print(target1.remove(source[1]))
print()
print(target2.index(source[4]))
print()
print(target1.find(source[0]))
print()
print(target2.peek())
print()
print("target1 and target2 are identical? " + str(target1.is_identical(target2)))
print()
print(target2.remove_front())
print()
target1.remove_many(source[2])

print("count of source[0] in target 1 is " + str(target1.count(source[0])))
print()
print("Min of target1 is:")
print(target1.min())
print()
print("Max of target2 is:")
print(target2.max())

print()
print(source[0] in target1)
print()
print(target1.__getitem__(1))
target1.clean()

print()
target3 = Sorted_List()
target3.intersection(target1, target2)
print("target 3 values intersection with target 1 and 2")
for a in target3:
    print(a)
    
print()
print("target 3 values union with target 1 and 2")
target3.union(target1, target2)
for a in target3:
    print(a)
    
print()
x,y = target1.split()
for a in x:
    print(a)

print()
x,y = target2.split_alt()
for a in y:
    print(a)
    
print()    
x,y = target1.split_key(source[0])
for a in x:
    print(a)
print()
for a in y:
    print(a)