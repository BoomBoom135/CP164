"""
-------------------------------------------------------
t01
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""
# Imports
from Queue_linked import Queue

target = Queue()
for i in range(1, 11):
    target.insert(i)
print(target._front._value)

source = Queue()
for i in range(1, 11):
    source.insert(i)
print(source._front._value)


target._move_front_to_rear(source)
