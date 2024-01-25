"""
-------------------------------------------------------
t08
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2024-01-09"
-------------------------------------------------------
"""
# Imports
from functions import matrix_stats

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
small, large, total, average = matrix_stats(a)
print(small, large, total, average)
