'''

--------------------------------------------
[CP164 A1]
--------------------------------------------

Author: Nabeel Shaikh
ID: 190741640
Email: shai1640@mylaurier.ca
__updated__:
---------------------------------------------
'''
# Imports





 
def hash_table(slots, values):
    """
    Use: hash_table(slots,values)
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
Hash     Slot Key
-------- ---- --------------------
 1652346    3 Dark City, 1998
  848448    6 Zulu, 1964
    Do not create an actual Hash_Set.
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """
    print("Hash     Slot Key")
    print("-------- ---- --------------------")
    for x in values:
        hash_value = hash(x)
        index = hash_value%slots
        key = x
        
        print("{:8d} {:4d} {:}".format(hash_value,index,key))
    return
    
    