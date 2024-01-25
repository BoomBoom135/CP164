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
from Queue_circular import Queue


q = Queue()

while True:
    ar = input("Add(a) or Remove(r): ")
    if ar == "a":
        q.insert(1)
    elif ar == "r":
        q.remove()
    else:
        continue
    print(q._values, q._front, q._rear)
