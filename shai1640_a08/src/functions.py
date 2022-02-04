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
from Letter import Letter
from BST_linked import BST



def do_comparisons(file_variable, bst):
    """
    -------------------------------------------------------
    Retrieves every letter in file_variable from bst. Generates
    comparisons in bst objects. Each Letter object in bst contains
    the number of comparisons found by searching for that Letter
    object in file_variable.
    Use: do_comparisons(file_variable, bst)
    -------------------------------------------------------
    Parameters:
        file_variable - the already open file containing data to evaluate (file)
        bst - the binary search tree containing 26 Letter objects
            to retrieve data from (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    file_variable.seek(0)
    for line in file_variable:
        for x in line:
            if x is not None and x.isalpha():
                val = Letter(x.upper())
                bst.retrieve(val)
                
        
    return 

    
    
    
def comparison_total(bst):
    """
    -------------------------------------------------------
    Sums the comparison values of all Letter objects in bst.
    Use: total = comparison_total(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        total - the total of all comparison fields in the bst
            Letter objects (int)
    -------------------------------------------------------
    """
    total = 0
    lst = bst.inorder()
    for x in lst:
        total += x.comparisons
    return total
    
def letter_table(bst):
    """
    -------------------------------------------------------
    Prints a table of letter counts for each Letter object in bst.
    Use: letter_table(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    total = 0
    lst = bst.inorder()
    for x in lst:
        total += x.count
    print("Letter Count/Percent Table")
    print()
    print("Total Count: " + str(total))
    print()
    print("Letter  Count       %")
    print("---------------------")
    for x in lst:
        print("{:>6s}  {:>2d}  {:>8.2f}%".format(x.letter,x.count,(x.count/total)*100))
    
