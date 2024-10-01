"""
-------------------------------------------------------
Assignment 3, Task 4
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-10-22"
-------------------------------------------------------
"""
# Imports

# Constants
from functions import multiply_fractions
num1 = int(input("Numerator 1: "))
denom1 = int(input("Denominator 1: "))
num2 = int(input("Numerator 2: "))
denom2 = int(input("Denominator 2: "))
numerator, denominator, product = multiply_fractions(
    num1, denom1, num2, denom2)
print(f'')
print(f'Result: {numerator:d}/{denominator:d} = {product:.3f}')
