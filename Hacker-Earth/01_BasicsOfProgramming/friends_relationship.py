"""
    Author: Punit Grewal
    Year: 2019
    Github: https://github.com/punit144/Competitive-Programming
    Problem: HackerEarth <
    Complexity:
"""
TEST = int(input())
for lp_1 in range(TEST):
    VALUE = int(input())
    STAR = 1
    HASH = (VALUE*2) - 2
    for lp_2 in range(VALUE):
        print("*"*STAR, end="")
        print("#"*HASH, end="")
        print("*"*STAR)
        STAR += 1
        HASH -= 2
    print()
    print()
