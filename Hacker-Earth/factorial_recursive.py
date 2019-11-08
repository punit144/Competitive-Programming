#!/usr/bin/python3
"""
    Author: Punit Grewal
    Github: https://github.com/punit144/Code-Monk
"""


def factorial(val_n):
    """
        This function calculates factorial of value val_n
    """
    if val_n in (1, 0):
        return 1
    return val_n * factorial(val_n - 1)


NUMBER = int(input())
print(factorial(NUMBER))
