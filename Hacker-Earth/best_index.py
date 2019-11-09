"""
    Author: Punit Grewal
    GitHub: https://github.com/punit144/Code-Monk
"""
ELEMENT = int(input())
ARRAY = list(map(int, input().split()))

# [1, 2, 3, 4, 5, 6, 0]

ARRAY.append(0)
#Variable Declaration
CTR = 0
END_CTR = 2
I_SUM = 0
MAX_SUM = ARRAY[-2]
# print(ARRAY)
for i in range(-2, -ELEMENT-2, -1):
    ARRAY[i] = ARRAY[i] + ARRAY[i+1]

    if CTR == END_CTR:
        CTR = 0
        END_CTR += 1
        I_SUM = ARRAY[i]
    else:
        I_SUM = ARRAY[i] - ARRAY[-1-CTR]

    if I_SUM > MAX_SUM:
        MAX_SUM = I_SUM

    CTR += 1
print(MAX_SUM)
