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
from List_array import List
from Food_utilities import read_foods

file = open("foods.txt","r")
source = read_foods(file)
target1 = List()
target2 = List()
target3 = List()

for x in range(0,5,1):
    target1.append(source[x])
    
for x in range(2,7,1):
    target2.append(source[x])


print("target1 is identical to target2? " + str(target1.is_identical(target2)))
print()

print(target1.remove(source[0]))


print()
print("target 2 get item at index 1 : " + str(target2.__getitem__(1)))
print()
print("Cleaning target2")
target2.clean()


print()
print("intersection of target 1 and 2 onto target 3")
target3.intersection(target1, target2)
print("target 3 values:")
for x in target3:
    print(x)
    
print()
print("union of target 1 and 2 onto target 3")
target3.union(target1, target2)
print("target3 values:")
for x in target3:
    print(x)

print()
print("Prepending last food object to target 1")
target1.prepend(source[-1])
print(target1[0])
print()
print("remove front of target1")
print(target1.remove_front())

print()
print("Appending first food object to target 2")
target2.append(source[0])
print(target2[-1])

print()
print("Combining target 1 and 2 onto 3")
target3.combine(target1,target2)

print()
print("splitting target 3 and printing first half values")
x,y = target3.split()
for a in x:
    print(a)
    
print()
print("Split alt of target 1 and showing second list's values")
target1.append(source[0])
target1.append(source[1])
target1.append(source[2])
x,y = target1.split_alt()
for a in y:
    print(a)





