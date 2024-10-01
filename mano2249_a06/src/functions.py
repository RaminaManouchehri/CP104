"""
-------------------------------------------------------
Assignment 6, Functions
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-11-14"
-------------------------------------------------------
"""


def winner():
    """
    -------------------------------------------------------
    returns two numbers representing how many times the string "blue" 
    appeared in the input and how many times the string "grey" appeared in the input.
    Use: num_blue, num_grey = winner()
    -------------------------------------------------------
    Parameters:
        none
    Returns:
        num_blue - how many times the string "blue" appeared
        num_grey - how many times the string "grey" appeared
    ------------------------------------------------------
    """
    num_grey = 0
    num_blue = 0
    loop = True
    while True:
        colour = input("Enter the winning team: ")
        if colour == "grey":
            num_grey = num_grey + 1
        elif colour == "blue":
            num_blue = num_blue + 1
        elif colour == '':
            break
        else:
            print("Invalid team, Please enter again ")
    return num_blue, num_grey


def is_prime(num):
    """
    -------------------------------------------------------
    Determines if num is a prime number.
    Use: prime = is_prime(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int > 1)
    Returns:
        prime - True if num is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    f = 0
    factor = 2
    while factor <= num / 2:
        if num % factor == 0:
            f = 1
            break
        factor = factor + 1
    if f == 0:
        prime = True
    else:
        prime = False
    return prime


def interest_table(principal, rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal, rate, payment)
    -------------------------------------------------------
    Parameters:
        principal - original value of a loan (float > 0)
        rate - yearly interest rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    month = 0
    interest_month = (rate / 100) / 12
    balance = principal
    print(f'Principal:   ${principal:.2f}')
    print(f'Interest rate : {rate:.1f}%')
    print(f'Monthly payment: ${payment:.1f}')
    print("----------------------------------")
    print("Month Interest   Payment   Balance")
    print("----------------------------------")
    while balance > 0:
        month = month + 1
        interest = balance * interest_month
        balance = (balance + interest) - payment
        if (balance < 0):
            payment = balance + payment
            balance = 0
        print(f'{month:5}{interest:9.2f}{payment:10.2f}{balance:10.2f}')
    return


def digit_count(num):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: count = digit_count(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int)
    Returns:
        count - the number of digits in num (int)
    ------------------------------------------------------
    """
    count = 0
    num2 = num
    if num < 0:
        num = num * -1
    while num > 0:
        count = count + 1
        num = num // 10
    if num2 == 0:
        count = 1
    return count


def sum_factors(num):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = sum_factors(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int >= 1)
    Returns:
        total - the total of num's factors (int)
    ------------------------------------------------------
    """
    factor = 0
    total = 0
    while factor < num:
        factor = factor + 1
        if (num % factor) == 0:
            total = total + factor
            if factor == num:
                total = total - factor
    return total
