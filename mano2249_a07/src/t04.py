"""
-------------------------------------------------------
Assignment 7, Task 4
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-11-21"
-------------------------------------------------------
"""
# Imports

from functions import subtract_lists
# Constants

num = 1
minuend = []
while num != 0:
    num = int(input("Enter a positive number: "))
    if num > 0:
        minuend.append(num)
num2 = 1
subtrahend = []
while num2 != 0:
    num2 = int(input("Enter a positive number: "))
    if num2 > 0:
        subtrahend.append(num)
subtract_lists(minuend, subtrahend)
print(minuend)
