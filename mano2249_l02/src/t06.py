"""
-------------------------------------------------------
[Lab 2, Task 6]
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-09-24"
-------------------------------------------------------
"""
# Imports

# Constants
mortgage_principle = float(input("Mortgage principal ($): "))
num_years = float(input("Number of years: "))
yearly_rate = int(input("Yearly interest rate (%): "))
# Calculations
num_months = num_years * 12
monthly_rate = yearly_rate / 1200
monthly_payment = monthly_rate * (1 + monthly_rate) ** num_months
monthly_payment = monthly_payment / ((1 + monthly_rate) ** num_months - 1)
monthly_payment = mortgage_principle * monthly_payment
# Output
print("The monthly payments are: $ ", monthly_payment)
