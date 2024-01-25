"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2024-01-25"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
from functions import queue_split_alt

source = Queue()
for i in range(1, 11):
    source.insert(i)
print(source._values)
target1, target2 = queue_split_alt(source)
print(target1._values)
print(target2._values)
