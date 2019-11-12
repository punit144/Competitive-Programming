"""
    Author: Punit Grewal
    Year: 2019
    Github: https://github.com/punit144/Competitive-Programming
    Problem: HackerEarth <
    Complexity:
"""
N_WORK = int(input())

for lp_1 in range(N_WORK):
    S_HR, S_MIN, E_HR, E_MIN = map(int, input().split())
    START = (S_HR*60) + S_MIN
    END = (E_HR*60) + E_MIN
    OUT_S = int(END - START)
    OUT_A = OUT_S // 60
    OUT_B = OUT_S % 60
    print(OUT_A, OUT_B, sep=" ")
