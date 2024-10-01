"""
-------------------------------------------------------
Assignment 2, Task 4
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-10-10"
-------------------------------------------------------
"""
# Imports

# Program
num_pieces = int(input("Number of pieces of cake: "))
num_partygoers = int(input("Number of party-goers: "))

# Calculations
cake_recieved = num_pieces // num_partygoers
undistributed_cake = num_pieces % num_partygoers
# Output
print(f"")
print(f"Each party-goer receives {cake_recieved:d} pieces of cake")
print(f"Pieces of cake that won’t be distributed: {undistributed_cake:d}")
