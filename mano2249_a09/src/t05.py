"""
-------------------------------------------------------
Assignment 9, Task 5
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-12-05"
-------------------------------------------------------
"""
# Imports
from functions import student_info
# Constants
students = open("students.txt", "r", encoding="utf-8")
l_id, h_id, avg = student_info(students)
students.close()
print(f"('{l_id}', '{h_id}', {avg:.2f})")
