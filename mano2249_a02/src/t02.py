"""
-------------------------------------------------------
Assignment 2, Task 2
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-10-10"
-------------------------------------------------------
"""
# Imports

# Constants
num = int(input("Enter a positive digit number: "))
num1 = num // 10
num2 = num % 10
product = num1 * num2
print("")
print(f'The product of the digits of {num:d} is {product:d}')
