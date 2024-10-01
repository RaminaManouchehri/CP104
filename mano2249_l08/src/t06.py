"""
-------------------------------------------------------
Lab 8, Task 6
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-11-10"
-------------------------------------------------------
"""
# Imports
from functions import list_stats
# Constants

num_values = int(input("How many values: "))
values = []
for i in range(num_values):
    a = float(input("Enter new number: "))
    values.append(a)


smallest, largest, total, average = list_stats(values)
print(f'({smallest:.0f}, {largest:.0f}, {total:.0f}, {average:.1f})')
