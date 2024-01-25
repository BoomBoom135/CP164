"""
-------------------------------------------------------
t06
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2024-01-25"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue

source = Priority_Queue()
for i in range(1, 10):
    source.insert(i)
key = 7
print(source._values, key)
target1, target2 = source.split_key(key)
print(target1._values)
print(target2._values)
