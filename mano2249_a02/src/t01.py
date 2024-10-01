"""
-------------------------------------------------------
Assignment 2, Task 1
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-10-10"
-------------------------------------------------------
"""
# Imports

# Constants
ANNUAL_TAX = 0.185
# Program
total_sales = float(input("Enter the total sales: $"))
tax = total_sales * ANNUAL_TAX
print(f"")
print(f"Projected Tax Report")
print(f"--------------------------")
print(f"Total sales:   $ {total_sales:,.2f}")
print(f"Annual tax:    % 18.50")
print(f"--------------------------")
print(f"Tax:           $  {tax:,.2f}")
