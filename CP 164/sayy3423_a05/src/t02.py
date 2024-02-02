"""
-------------------------------------------------------
t02
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2024-02-02"
-------------------------------------------------------
"""
# Imports
from Sorted_List_array import Sorted_List
from random import randint

source1 = Sorted_List()
for i in range(1, 11):
    source1.insert(randint(1, 10))

source2 = Sorted_List()
for i in range(1, 11):
    source2.insert(randint(1, 10))

print(source1._values, source2._values)
equals = source1 == source2
print(equals)
