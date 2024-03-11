"""
-------------------------------------------------------
t01
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2024-03-11"
-------------------------------------------------------
"""
# Imports
from functions import hash_table
from Food_utilities import read_foods

file = open('foods.txt', 'r')
foods = read_foods(file)
hash_table(7, foods)
file.close()
