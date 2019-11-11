"""
    Author: Punit Grewal
    Year: 2019
    Github: https://github.com/punit144/Competitive-Programming
    Problem: HackerEarth < Basics of Programming
    Complexity: Easy
"""
AXIS = [0, 0]
IN_STR = str(input())

for lp_1 in IN_STR:
    if lp_1 == 'L':
        AXIS[0] -= 1
    elif lp_1 == 'R':
        AXIS[0] += 1
    elif lp_1 == 'U':
        AXIS[1] += 1
    else:
        AXIS[1] -= 1

print(*AXIS)
