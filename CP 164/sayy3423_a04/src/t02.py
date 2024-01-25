"""
-------------------------------------------------------
t02
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2024-01-25"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue


q = Queue()
a = Queue()

for i in range(1, 11):
    q.insert(i)

for i in range(10, 0, -1):
    a.insert(i)

equals = q == a
print(q._values)
print(a._values)
print(equals)
