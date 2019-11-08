"""
    Author: Punit Grewal
    GitHub: https://github.com/punit144/Code-Monk
"""
CODE_WORD = str(input())
KEY = int(input())
AL_STR = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
AL_STR_LOW = "abcdefghijklmnopqrstuvwxyz"
NUM_STRING = "0123456789"
AD = {}
AD_LOW = {}
ND = {}
COUNTER = 0
for char in AL_STR:
    AD[COUNTER] = char
    COUNTER += 1

COUNTER = 0
for char_lower in AL_STR_LOW:
    AD_LOW[COUNTER] = char_lower
    COUNTER += 1

COUNTER = 0
for num in NUM_STRING:
    ND[COUNTER] = num
    COUNTER += 1

RORATION = 0
T_KEY = 0
CIPHERED_CODE = ""
for cipher in CODE_WORD:
    if cipher in AL_STR:
        T_KEY = list(AD.keys())[list(AD.values()).index(cipher)]
        ROTATION = T_KEY
        for lp_1 in range(KEY):
            if ROTATION < 25:
                ROTATION += 1
            else:
                ROTATION = 0
        CIPHERED_CODE += AD[ROTATION]
    elif cipher in AL_STR_LOW:
        T_KEY = list(AD_LOW.keys())[list(AD_LOW.values()).index(cipher)]
        ROTATION = T_KEY
        for lp_2 in range(KEY):
            if ROTATION < 25:
                ROTATION += 1
            else:
                ROTATION = 0
        CIPHERED_CODE += AD_LOW[ROTATION]
    elif cipher in NUM_STRING:
        T_KEY = list(ND.keys())[list(ND.values()).index(cipher)]
        ROTATION = T_KEY
        for lp_1 in range(KEY):
            if ROTATION < 9:
                ROTATION += 1
            else:
                ROTATION = 0
        CIPHERED_CODE += ND[ROTATION]
    else:
        CIPHERED_CODE += cipher
# print(AD, AD_LOW, ND)
print(CIPHERED_CODE)
