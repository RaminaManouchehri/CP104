"""
-------------------------------------------------------
Lab 4, Task 9
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-10-05"
-------------------------------------------------------
"""
# Imports
from functions import fraction_product
num1 = int(input("Enter the numerator of the first fraction: "))
den1 = int(input("Enter the denominator of the first fraction: "))
num2 = int(input("Enter the numerator of the second fraction: "))
den2 = int(input("Enter the denominator of the second fraction: "))

# Output
num, den, product = fraction_product(num1, den1, num2, den2)
print(f'({num:d}, {den:d}, {product:.2f})')
