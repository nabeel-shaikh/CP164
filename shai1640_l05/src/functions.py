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

def recurse(x, y):
    """
    -------------------------------------------------------
    Recursive function - example of tree recursion.
    Use: ans = recurse(x, y)
    -------------------------------------------------------
    Parameters:
        x - an integer (int)
        y - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    if x<0 or y<0:
        ans = x-y
    else:
        ans = recurse(x-1, y) + recurse(x, y-1)
    return ans


def gcd(m, n):
    """
    -------------------------------------------------------
    Recursively find the Greatest Common Denominator of two numbers.
    Use: ans = gcd(m, n)
    -------------------------------------------------------
    Parameters:
        n - an integer (int)
        m - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    if m%n == 0:
        ans = n
    else:
        ans = gcd(n, m%n)
    return ans
        
        
def vowel_count(s):
    """
    -------------------------------------------------------
    Recursively counts number of vowels in a string.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - string to examine (str)
    Returns:
        count - number of vowels in s (int)
    -------------------------------------------------------
    """
    vowels = "aeiou"
    if len(s) == 0:
        count = 0
    elif len(s) == 1 and s[0].lower() in vowels:
        count = 1
    elif len(s) > 1 and s[0].lower() in vowels:
        count = 1 + vowel_count(s[1:])
    else:
        count = vowel_count(s[1:])
        
    return count
    
def to_power(base, power):
    """
    -------------------------------------------------------
    Calculates base^power.
    Use: ans = to_power(base, power)
    -------------------------------------------------------
    Parameters:
        base - base to apply power to (float)
        power - power to apply (int)
    Returns:
        ans - base ^ power (float)
    -------------------------------------------------------
    """
    if power == 0:
        ans =  1
    
    elif power == 1:
        ans = base*1
        
    elif power == -1:
        ans = 1/base
    
    else:
        if power<0:
            ans = to_power(base, power+1)/base
        else:
            ans = base*to_power(base, power-1) 
         
    
    return ans    


def is_palindrome(s):
    """
    -------------------------------------------------------
    Recursively determines if s is a palindrome. Ignores non-letters and case.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    new = ""
    for x in s:
        if x.isalpha():
            new = new + x.lower()
            
    
    if len(new) == 0 or len(new) == 1:
        palindrome = True
    else:
        if new[0] == new[-1]:
            palindrome = is_palindrome(new[1:-1])
        else:
            palindrome = False
    return palindrome
           



def bag_to_set(bag):
    """
    -------------------------------------------------------
    Copies elements of a bag to a set.
    Use: new_set = bag_to_set(bag)
    -------------------------------------------------------
    Parameters:
        bag - a list of values (list)
    Returns:
        new_set - containing one each of the elements in bag (list)
    -------------------------------------------------------
    """
    new_set = []
    if len(bag) == 0:
        new_set = []
         
    elif bag[-1] in bag[:-1]:
        new_set = bag_to_set(bag[:-1])
        
        
    else:
        new_set = bag_to_set(bag[:-1]) + [bag[-1]]

            
        
    return new_set
    
    
print(bag_to_set([1,2,3,3,3,3,3,4]))
    
    
    
    
    
    
    
        