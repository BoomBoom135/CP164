"""
-------------------------------------------------------
t02
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2024-01-11"
-------------------------------------------------------
"""
# Imports
from Food_utilities import average_calories
from Food_utilities import read_foods

file_variable = open("foods.txt", "r")
foods = read_foods(file_variable)
avg = average_calories(foods)
print(avg)
