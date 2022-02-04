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

from functions import postfix

string = "12 5 -"
answer = postfix(string)
print(answer)

string = "4 5 + 12 * 2 3 * -"
answer = postfix(string)
print(answer)