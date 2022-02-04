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
# Imports
from random import randint, random

from List_linked import List
from Number import Number
from Sorts_List_linked import Sorts


# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted List of Number objects.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """
    values = List()
    for i in range(0,SIZE):
        val = Number(i)
        values.append(val)

    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed List of Number objects.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """
    values = List()
    for i in range(SIZE-1,-1,-1):
        val = Number(i)
        values.append(val)

    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        lists - TEST lists of SIZE Number objects containing
            values between 0 and XRANGE (list of List of Number)
    -------------------------------------------------------
    """
    lists = List()
    for i in range(0,TESTS):
        lst = List()
        for x in range(0,SIZE):
            number = randint(0,XRANGE)
            val = Number(number)
            lst.append(val)
        lists.append(lst)

    return lists


def test_sort(title, func):
    """
    -------------------------------------------------------
    Tests a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of Lists in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """
    sorted_values = create_sorted()
    reversed_values = create_reversed()
    random_values = create_randoms()
    
    Number.comparisons = 0
    Sorts.swaps = 0
    func(sorted_values)
    sorted_swaps = Sorts.swaps
    sorted_comparisons = Number.comparisons
    
    Number.comparisons = 0
    Sorts.swaps = 0
    func(reversed_values)
    reversed_swaps = Sorts.swaps
    reversed_comparisons = Number.comparisons
    
    Number.comparisons = 0
    Sorts.swaps = 0
    for a in random_values:
        func(a)
    random_swaps = Sorts.swaps
    random_comparisons = Number.comparisons
    
    print("n:   100       |      Comparisons       | |         Swaps          |")
    print("Algorithm      In Order Reversed   Random In Order Reversed   Random")
    print('-------------- -------- -------- -------- -------- -------- --------')
    print("{:<14s} {:>8.0f} {:>8.0f} {:>8.0f} {:>8.0f} {:>8.0f} {:>8.0f}".format(title,sorted_comparisons,reversed_comparisons,random_comparisons,sorted_swaps,reversed_swaps,random_swaps))
    
    return


