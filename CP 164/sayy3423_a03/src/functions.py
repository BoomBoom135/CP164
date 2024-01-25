"""
-------------------------------------------------------
functions for a03
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2024-01-17"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from utilities import stack_to_array
from utilities import array_to_stack

# function t01


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

    while not source1.is_empty() or not source2.is_empty():
        if not source1.is_empty():
            target.push(source1.pop())
        if not source2.is_empty():
            target.push(source2.pop())

    return target


# function t03


def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    temp = []
    stack_to_array(source, temp)
    array_to_stack(source, temp)

# function t05


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
    palindrome = True
    stack = Stack()
    for let in string:
        stack.push(let)

    while not stack.is_empty():
        if stack.pop() != string[0]:
            palindrome = False
        string = string[1:]

    return palindrome


# function t06
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
    stack = Stack()
    el = string.split()
    for e in el:
        if e not in OPERATORS:
            stack.push(e)
        else:
            first = float(stack.pop())
            second = float(stack.pop())
            if e == "+":
                stack.push(second+first)
            elif e == "-":
                stack.push(second-first)
            elif e == "*":
                stack.push(second*first)
            else:
                stack.push(second/first)

    answer = stack.pop()
    return answer


# function t07


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
    path = []
    now = 'Start'
    options = maze[now]

    if "X" in options:
        path.append("X")
    stack = Stack()
    while "X" not in options:
        for d in options:
            stack.push(d)
        now = stack.pop()
        if maze[now] != []:
            path.append(now)
        options = maze[now]
        if "X" in options:
            path.append("X")

    return path
