"""
-------------------------------------------------------
Assignment 1, Task 4
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-10-06"
-------------------------------------------------------
"""
# Imports

# Constants

# Program
pizza_cost = float(input("Cost of 1 pizza slice: $"))
num_slices = int(input("Number of pizza slices: "))

# Calculations
total_cost = pizza_cost * num_slices

# Output
print(f'Total cost of {num_slices} pizza slices: $ {total_cost:.2f}')
