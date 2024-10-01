"""
-------------------------------------------------------
Lab 4, Task 8
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-10-05"
-------------------------------------------------------
"""
# Imports
from functions import computer_costs
computer_cost = float(input("Enter the cost of the computer: "))
computers_bought = int(input("Enter the number of computers bought: "))
commission_percent = float(input("Enter the percent of commission: "))

# Constants
pre_commission_cost, total_cost = computer_costs(
    computer_cost, computers_bought, commission_percent)
print(f"({pre_commission_cost:.2f}, {total_cost:.2f})")
