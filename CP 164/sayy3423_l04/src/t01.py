"""
-------------------------------------------------------
t01
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2024-01-25"
-------------------------------------------------------
"""
# Imports
from List_array import List

l = List()
for i in range(1, 11):
    l.append(i)

l.insert(-100, 5)
print(l._values)
