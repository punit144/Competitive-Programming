"""
    Author: Punit Grewal
    Year: 2019
    Github: https://github.com/punit144/Competitive-Programming
    Problem: HackerEarth <
    Complexity:
"""
TEST = int(input())
INPUT_N = ''
LIFT_A = 0
LIFT_B = 7

for lp_1 in range(TEST):
    INPUT_N = int(input())
    CALL_1 = abs(INPUT_N - LIFT_A)
    CALL_2 = abs(INPUT_N - LIFT_B)
    if CALL_1 <= CALL_2:
        print("A")
        LIFT_A = INPUT_N
    else:
        print("B")
        LIFT_B = INPUT_N
