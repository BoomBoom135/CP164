"""
-------------------------------------------------------
t04
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2024-01-09"
-------------------------------------------------------
"""
# Imports
from functions import file_analyze

fv = open("words.txt", "r", encoding="utf-8")
upp, low, dig, whi, rem = file_analyze(fv)
print(upp, low, dig, whi, rem)
