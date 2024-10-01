"""
-------------------------------------------------------
Functions
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-10-18"
-------------------------------------------------------
"""
# Imports
import math
# Constants


def gym_cost(cost, friends):
    """
    -------------------------------------------------------
    Calculates total cost of a gym membership. A member gets a
    discount according to the number of friends they sign up.
        0 friends: 0% discount
        1 friend: 5% discount
        2 friends: 10% discount
        3 or more friends: 15% discount
    Use: final_cost = gym_cost(cost, friends)
    -------------------------------------------------------
    Parameters:
        cost - a gym membership base cost (float > 0)
        friends - number of friends signed up (int >= 0)
    Returns:
        final_cost - cost of membership after discount (float)
    ------------------------------------------------------
    """
    DISCOUNT = 0.05
    if friends == 1:
        final_cost = cost - (cost * (DISCOUNT))
    elif friends == 2:
        final_cost = cost - (cost * (DISCOUNT * 2))
    elif friends >= 3:
        final_cost = cost - (cost * (DISCOUNT * 3))

    else:
        final_cost = cost

    return final_cost


def is_leap(year):
    """
    -------------------------------------------------------
    Determines if a year is a leap year. Every year that is
    exactly divisible by four is a leap year, except for years
    that are exactly divisible by 100, but these centurial years
    are leap years if they are exactly divisible by 400. For
    example, the years 1700, 1800, and 1900 are not leap years,
    but the years 1600 and 2000 are.
    Use: result = is_leap(year)
    -------------------------------------------------------
    Parameters:
        year - a year (int > 0)
    Returns:
        result - True if year is a leap year,
            False otherwise (boolean)
    ------------------------------------------------------
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                result = True
            else:
                result = False
        else:
            result = True

    else:
        result = False

    return result


def get_pay(hourly_rate, hours_worked):
    """
    -------------------------------------------------------
    Calculates an employee's net wage given hours and pay.
    Each employee is paid 1.5 times their regular hourly rate for
    all hours over 40. A tax amount of 3.625 percent of gross salary
    is deducted.
    Use: net_payment = get_pay(hourly_rate, hours_worked)
    -------------------------------------------------------
    Parameters:
        hourly_rate - hourly rate of pay (float)
        hours_worked - total hours worked (float)
    Returns:
        net_payment - description (float)
    ------------------------------------------------------
    """
    OVERTIME_HOURS = 40
    OVERTIME_RATE = 1.5
    TAX_RATE = 0.03625
    if hours_worked <= OVERTIME_HOURS:
        net_payment = hourly_rate * hours_worked
        tax = net_payment * TAX_RATE
        net_payment = net_payment - tax

    else:
        net_payment = (hours_worked - OVERTIME_HOURS) * \
            (OVERTIME_RATE * hourly_rate) + hourly_rate * OVERTIME_HOURS
        tax = net_payment * TAX_RATE
        net_payment = net_payment - tax

    return net_payment


def pay_raise(status, years, salary):
    """
    -------------------------------------------------------
    Calculates pay raises for employees. Pay raises are based on:
    status: Full Time ('F)' or Part Time ('P')
    and years of service
    Raises are:
        5% for full time greater than or equal to 10 years service
        1.5% for full time less than 4 years service
        3% for part time greater than 10 years service
        1% for part time less than 4 years service
        2% for all others
    Use: new_salary = pay_raise(status, years, salary)
    -------------------------------------------------------
    Parameters:
        status - employment type (str - 'F' or 'P')
        years - number of years employed (int > 0)
        salary - current salary (float > 0)
    Returns:
        new_salary - employee's new salary (float).
    -------------------------------------------------------
    """
    BASIC_RAISE = 0.02
    F_RAISE_TEN_PLUS = 0.05
    F_RAISE_FOUR_LESS = 0.015
    P_RAISE_TEN_PLUS = 0.03
    P_RAISE_FOUR_LESS = 0.01

    if status == "F":
        if years >= 10:
            new_salary = salary + (salary * F_RAISE_TEN_PLUS)
        elif years < 4:
            new_salary = salary + (salary * F_RAISE_FOUR_LESS)
        else:
            new_salary = salary + (salary * BASIC_RAISE)

    else:
        if years >= 10:
            new_salary = salary + (salary * P_RAISE_TEN_PLUS)
        elif years < 4:
            new_salary = salary + (salary * P_RAISE_FOUR_LESS)
        else:
            new_salary = salary + (salary * BASIC_RAISE)

    return new_salary


def fast_food():
    """
    -------------------------------------------------------
    Food order function.
    Asks user for their order and if they want a combo, and if
    necessary, what is the side order for the combo:
    Prices:
        Burger: $6.00
        Wings: $8.00
        Fries combo: add $1.50
        Salad combo: add $2.00
    Use: price = fast_food()
    -------------------------------------------------------
    Returns:
        price - the price of one meal (float)
    -------------------------------------------------------
    """
    BURGER = 6.00
    WINGS = 8.00
    FRIES = 1.50
    SALAD = 2.00
    order = input("Order B - burger or W - wings: ")
    combo = input("Make it a combo? (Y/N): ")
    if order == "B":
        if combo == "Y":
            combo_order = input("Add F - fries or S - salad: ")
            if combo_order == "F":
                price = BURGER + FRIES
            else:
                price = BURGER + SALAD
        else:
            price = BURGER
    else:
        if combo == "Y":
            combo_order = input("Add F - fries or S - salad: ")
            if combo_order == "F":
                price = WINGS + FRIES
            else:
                price = WINGS + SALAD
        else:
            price = WINGS
    return price
