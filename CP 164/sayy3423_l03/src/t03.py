"""
-------------------------------------------------------
t03
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2024-01-24"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
from utilities import array_to_queue
from utilities import queue_to_array
from utilities import queue_test

source = [1, 2, 3, 4, 5, 6, 7, 8, 9]
queue = Queue()
array_to_queue(queue, source)
print(queue._values)

target = []
queue_to_array(queue, target)
print(target)

a = [5, 4, 3, 2, 1]
queue_test(a)
