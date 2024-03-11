"""
-------------------------------------------------------
t03
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2024-03-11"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from Letter import Letter
from functions import do_comparisons, comparison_total, letter_table

# Takes a Long Time to Compute

DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

bst1 = BST()
for value in DATA1:
    letter = Letter(value)
    bst1.insert(letter)

file = open('miserables.txt', 'r')
do_comparisons(file, bst1)
total = comparison_total(bst1)
file.close()

letter_table(bst1)
