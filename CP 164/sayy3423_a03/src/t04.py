"""
-------------------------------------------------------
t04
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2024-01-13"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from utilities import array_to_stack

source = Stack()
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
array_to_stack(source, list)
print("Before:", source._values)
source.reverse()
print("After:", source._values)
