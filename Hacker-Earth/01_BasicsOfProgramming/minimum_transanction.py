"""
    Author: Punit Grewal
    Year: 2019
    Github: https://github.com/punit144/Competitive-Programming
    Problem: HackerEarth <
    Complexity:
"""
"""
    Author: Punit Grewal
    Year: 2019
    Github: https://github.com/punit144/Competitive-Programming
    Problem: HackerEarth <
    Complexity:
"""
N, M = map(int, input().split())
LENTER = {}
OUTPUT = []

for lp_g1 in range(M):
    U, V, W = map(int, input().split())
    if U in LENTER:
        LENTER[U] = LENTER[U] - W
    else:
        LENTER[U] = -W
    if V in LENTER:
        LENTER[V] += W
    else:
        LENTER[V] = W
OUTPUT = sum(i for i in LENTER.values() if i < 0)
print(abs(OUTPUT))

