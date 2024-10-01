"""
-------------------------------------------------------
Assignment 7, Task 3
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-11-20"
-------------------------------------------------------
"""
# Imports
from functions import list_indexes
# Constants
num = 1
values = []
while num != 0:
    num = int(input("Enter a positive number: "))
    if num > 0:
        values.append(num)
target = int(input("Enter target value: "))

indexes = list_indexes(values, target)
print(indexes)
