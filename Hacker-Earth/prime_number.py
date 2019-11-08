"""
    Author: Punit Grewal
    GitHub: https://github.com/punit144/Code-Monk
    Description: This program provides list of all prime number
    input by the user
"""
USER_INPUT = int(input())
PRIME = []
for i in range(2, USER_INPUT):
    k = 0
    for pr in range(2, i):
        if i % pr == 0:
            k = 1
        else:
            continue
    if k == 0:
        PRIME.append(i)
print(*PRIME)
print(len(PRIME))
