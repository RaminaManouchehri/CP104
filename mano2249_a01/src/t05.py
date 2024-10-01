"""
-------------------------------------------------------
Assignment 1, Task 5
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-10-02"
-------------------------------------------------------
"""
# Imports

# Constants

# Program
principle = float(input("Principal: $"))
interest = float(input("Interest (decimal): "))
num_years = int(input("Number of years: "))
num_compounded = int(input("Number of times interest compounded per year: "))

# Calculations
balance = 1 + (interest / num_compounded)
balance = principle * (balance) ** (num_compounded * num_years)
print(f'Balance: $ {balance}')
