"""
    Author: Punit Grewal
    Year: 2019
    Github: https://github.com/punit144/Competitive-Programming
    Problem: HackerEarth <
    Complexity:
"""
N, M = map(int, input().split())
LENTER = {}
LEN_LST = []
REN_LST = []

for lp_g1 in range(M):
    U, V, W = map(int, input().split())
    if U in LENTER:
        LENTER[U] -= W
        OUTPUT += abs(w)
    else:
        LENTER[U] = -W
        LEN_LST.append(U)
    if V in LENTER:
        LENTER[V] += W
    else:
        LENTER[V] = W
        REN_LST.append(V)

OUTPUT = 0
CTR = 0
LENGTH = len(LEN_LST)
while 1:
    if LENTER[LEN_LST[CTR]] < 0:
        OUTPUT += abs(LENTER[LEN_LST[CTR]])
        CTR += 1
        if CTR == LENGTH:
            break
print(OUTPUT)
