"""
-------------------------------------------------------
t06
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2024-01-28"
-------------------------------------------------------
"""
# Imports
from utilities import array_to_list, list_to_array
from List_array import List

list = List()
source = [1, 2, 3, 4, 5]
array_to_list(list, source)
print(list._values)


target = []
list_to_array(list, target)
print(target)
