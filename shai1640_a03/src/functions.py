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
from Stack_array import Stack


def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    target1 = Stack()
    target2 = Stack()
    
    while not source.is_empty():
        target1.push(source.pop())
        if not source.is_empty():
            target2.push(source.pop())
    
    return target1, target2


def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    target = Stack()
    while not source1.is_empty() and not source2.is_empty():
        target.push(source1.pop())
        target.push(source2.pop())
        
    while not source1.is_empty():
        target.push(source1.pop)
    while not source2.is_empty():
        target.push(source2.pop())
    return target

def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    words = ""
    half_stack = Stack()
    
    
    for x in string:
        if x.isalpha():
            words += x.lower()
            
    if x == "":
        return True
            
    length = len(words)//2
    
    if len(words) % 2 != 0:
        for a in range(length + 1,len(words),1):
            half_stack.push(words[a])
        for a in range(0, length, 1):
            if half_stack.pop() != words[a]:
                return False
        return True    
            
    if len(words) % 2 == 0:
        for a in range(length,len(words),1):
            half_stack.push(words[a])
        for a in range(0,length,1):
            if half_stack.pop() != words[a]:
                return False
        return True
    
    
    
    
# Constants
OPERATORS = "+-*/"
def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    string = string.split(" ")
    values = Stack()
    for x in string:
        if x.isdigit():
            values.push(int(x))
        elif x in OPERATORS:
            right = values.pop()
            left = values.pop()
            if x == "-":
                values.push(left - right)
            elif x== "+":
                values.push(left + right)
            elif x == "*":
                values.push(left*right)
            else:
                values.push(left/right)
    return values.pop()
def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            None if there is no exit (list of str)
    -------------------------------------------------------
    """
    
    paths = Stack()
    for x in maze["Start"]:
        paths.push(x)
        
    
    
    


            

                
            
            
            
                    
        
    
    
            
    
    


        

