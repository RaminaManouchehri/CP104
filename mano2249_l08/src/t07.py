"""
-------------------------------------------------------
Lab 8, Task 7
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-11-10"
-------------------------------------------------------
"""
# Imports
from functions import list_categorize
# Constants
num_values = int(input("How many values: "))
values = []
for i in range(num_values):
    a = float(input("Enter new number: "))
    values.append(a)

negatives, positives, zeroes, evens, odds = list_categorize(values)

print(f'({negatives}, {positives}, {zeroes}, {evens}, {odds})')
