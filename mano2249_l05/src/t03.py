"""
-------------------------------------------------------
Lab 5, Task 3
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-10-18"
-------------------------------------------------------
"""
# Imports
from functions import gym_cost
cost = float(input("Enter gym membership base cost: "))
friends = int(input("Enter number of friends: "))
final_cost = gym_cost(cost, friends)
print(f'{final_cost:.2f}')
