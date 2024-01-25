"""
-------------------------------------------------------
t05
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2024-01-11"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods
from Food_utilities import food_search

file_variable = open("foods.txt", "r")
foods = read_foods(file_variable)
origin = int(input("Origin: "))
max_cals = int(input("Max Cals: "))
is_veg = input("Is vegetarian(True/False): ")
results = food_search(foods, origin, max_cals, is_veg)
for food in results:
    print(food)
