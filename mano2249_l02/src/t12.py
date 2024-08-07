"""
-------------------------------------------------------
[Lab 2, Task 12]
-------------------------------------------------------
__updated__ = "2022-09-24"
-------------------------------------------------------
"""
# Imports

# Constants
SECONDS_MIN = 60
# Program
seconds = int(input("Number of seconds: "))
# Calculations
mins_total = seconds // SECONDS_MIN
days = mins_total // 1440
mins_total2 = mins_total % 1440
hours = mins_total2 // 60
mins_total2 = mins_total2 % 60
minutes = mins_total2 // 1
mins_total2 = mins_total2 % 1
seconds2 = seconds - (mins_total * 60)
# Output
print("Days:", days, end="")
print(" Hours:", hours, end="")
print(" Minutes:", minutes, end="")
print(" seconds:", seconds2)
