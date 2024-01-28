"""
-------------------------------------------------------
t06
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2024-01-26"
-------------------------------------------------------
"""
# Imports
from utilities import array_to_list, list_to_array
from List_array import List

list = List()
source = [1, 2, 3, 4, 5]
array_to_list(list, source)
print(list._values)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = List()
list_to_array(list, target)
print(target._values)
