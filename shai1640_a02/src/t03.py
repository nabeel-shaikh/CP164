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
from Food_utilities import calories_by_origin
from Food import Food

a = Food("Butter Chicken", 2, False, 500)
b = Food("Jamaican Chicken", 4, False, 550)
c = Food("Mashed Patotoes", 8, True, 250)
d = Food("Tandoori Chicken", 2, False, 400)
foods = [a,b,c,d]

a = calories_by_origin(foods, 2)

print(a)