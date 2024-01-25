"""
-------------------------------------------------------
t06
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2024-01-24"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue
from utilities import array_to_pq
from utilities import pq_to_array
from utilities import priority_queue_test

source = [4, 2, 5, 7, 6, 8, 9, 3]
pq = Priority_Queue()
array_to_pq(pq, source)
print(pq._values)

target = []
pq_to_array(pq, target)
print(target)

a = [9, 6, 8, 4, 6, 5, 3, 2, 4]
priority_queue_test(a)
