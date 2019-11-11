"""
    Author: Punit Grewal
    Year: 2019
    Github: https://github.com/punit144/Competitive-Programming
    Problem: HackerEarth <
    Complexity:
"""
WORK = 1

N_BRIK = int(input())
OUTPUT = 0

while 1:
    OUTPUT += WORK
    if OUTPUT >= N_BRIK:
        print("Patlu")
        break
    OUTPUT += WORK*2
    if OUTPUT >= N_BRIK:
        print("Motu")
        break
    WORK += 1
