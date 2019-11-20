"""
    Author: Punit Grewal
    Year: 2019
    Github: https://github.com/punit144/Competitive-Programming
    Problem: HackerEarth <
    Complexity:
"""
N = int(input())
ARR = list(map(int, input().split()))
BRR = [0] * (N+2)
QRY = int(input())

for lp_g1 in range(QRY):
    Q1, Q2 = list(map(int, input().split()))
    BRR[Q1] ^= 1
    BRR[Q2+1] ^= 1

for lp_g2 in range(1, N+1, 1):
    BRR[lp_g2] ^= BRR[lp_g2-1]

for lp_g4 in range(1, N+1, 1):
    ARR[lp_g4-1] = ARR[lp_g4-1] ^ BRR[lp_g4]
BRR.clear()
print(sum(ARR))
print(*ARR)
