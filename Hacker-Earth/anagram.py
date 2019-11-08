#!/usr/bin/python3
"""
    Author: Punit Grewal
    Github : https://github.com/punit144/Code-Monk
"""


def anagram_func(arg_1, arg_2):
    """
        This function takes two strings as input and returns
        number of chracter which needs to be deleted so that
        can be an anagram.
    """
    arg_1.lower()
    arg_2.lower()
    str_compute = {}
    char_count = 0
    for lp_1 in arg_1:
        if lp_1 not in str_compute:
            str_compute[lp_1] = 1
        else:
            str_compute[lp_1] += 1
    print(str_compute)
    for lp_2 in arg_2:
        if lp_2 not in str_compute:
            char_count += 1
        else:
            if str_compute[lp_2] == 0:
                char_count += 1
            else:
                str_compute[lp_2] -= 1
    print(str_compute)
    for lp_3 in str_compute.values():
        char_count += lp_3

    print(char_count)


# Global Variables
TEST_CASE = int(input())
INPUT_STRING = {}

# Create Dictionary with one key two values as two strings of anagram
for i in range(TEST_CASE):
    INPUT_STRING[i] = str(input()), str(input())

print(INPUT_STRING[0])

# Pass the each item of dictionary to function and get the required output.
for j in INPUT_STRING.values():
    anagram_func(j[0], j[1])
