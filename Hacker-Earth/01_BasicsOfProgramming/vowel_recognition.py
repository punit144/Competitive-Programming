"""
    Author: Punit Grewal
    Year: 2019
    Github: https://github.com/punit144/Competitive-Programming
    Problem: HackerEarth < Time Complexity
    Complexity: Medium
"""
TEST = int(input())
for lp_1 in range(TEST):
    STRING = input()
    COMPARE = "aeiouAEIOU"
    LENGTH = len(STRING)
    VOW_DIC = {}
    for VOW_LOC, VOW_VAL in enumerate(STRING):
        if VOW_VAL in COMPARE:
            VOW_DIC[VOW_LOC] = VOW_VAL
    OUTPUT = 0
    for lp_3 in VOW_DIC:
        OUTPUT += (LENGTH-lp_3)*(lp_3+1)
print(OUTPUT)
