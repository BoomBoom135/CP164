"""
-------------------------------------------------------
t07
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2024-01-17"
-------------------------------------------------------
"""
# Imports
from functions import stack_maze

maze = {'Start': ['A'], 'A': ['B', 'C'], 'B': [], 'C': ['D', 'E'],
        'D': [], 'E': ['F', 'X'], 'F': ['G', 'H'], 'G': [], 'H': []}
path = stack_maze(maze)
print("Path:", path)
