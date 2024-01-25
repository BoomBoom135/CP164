"""
-------------------------------------------------------
t01
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2024-01-11"
-------------------------------------------------------
"""
# Imports
from utilities import array_to_stack
from utilities import stack_to_array
from utilities import stack_test
from Food_utilities import read_foods
from Stack_array import Stack

s = Stack()
b = s.is_empty()

value = int(input("Value: "))
s.push(value)
value = s.peek()
value = s.pop()

stack = Stack()
source = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = []

array_to_stack(stack, source)

stack_to_array(stack, target)

stack_test(source)

fh = open("foods.txt", "r")
source = read_foods(fh)
stack_test(source)
fh.close()
