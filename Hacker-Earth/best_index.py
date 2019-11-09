"""
    Author: Punit Grewal
    GitHub: https://github.com/punit144/Code-Monk
"""
ELEMENT = int(input())
ARRAY = list(map(int, input().split()))

ARRAY.append(0)

#Variable Declaration
CTR = 0
END_CTR = 2
I_SUM = ARRAY[ELMENT-2]
MAX_SUM = 0
# print(ARRAY)
for i in range(-3, -ELEMENT-2, -1):
    if CTR == END_CTR:
        CTR = 0
        END_CTR += 1
    
    ARRAY[i] = ARRAY[i+1]

