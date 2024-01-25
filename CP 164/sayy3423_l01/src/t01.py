"""
-------------------------------------------------------
t01
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2024-01-10"
-------------------------------------------------------
"""
# Imports
from Food import Food
from Food_utilities import get_food
from Food_utilities import read_food
from Food_utilities import read_foods
from Food_utilities import write_foods
from Food_utilities import get_vegetarian
"""
source = get_food()
s = Food(source[0], source[1], source[2], source[3])
print("\n" + str(s))

line = input("\nFood Info: ")
source = read_food(line)
print(source)
"""
file_variable = open("foods.txt", "r")
foods = read_foods(file_variable)
file_variable.close()

file_variable = open("new_foods.txt", "w")
write_foods(file_variable, foods)
file_variable.close()

v_foods = get_vegetarian(foods)
