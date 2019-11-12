"""
    Author: Punit Grewal
    Year: 2019
    Github: https://github.com/punit144/Competitive-Programming
    Problem: HackerEarth < Time Complexity
    Complexity: Medium
"""
"""
    Author: Punit Grewal
    Year: 2019
    Github: https://github.com/punit144/Competitive-Programming
    Problem: HackerEarth < Time Complexity
    Complexity: Medium
"""
"""
    Author: Punit Grewal
    Year: 2019
    Github: https://github.com/punit144/Competitive-Programming
    Problem: HackerEarth < Time Complexity
    Complexity: Medium
"""
TEST = int(input())
for lp_t in range(TEST):
    STRING = input()
    STRING = STRING.lower()
    SUB_STRING = []
    CTR = 0
    CTR_N = len(STRING) - 1
    IDX = 0
    CTR_1 = 0
    CTR_2 = 1
    T_STR = ''
    while 1:
        if CTR_1 < CTR_2:
            T_STR = T_STR + STRING[IDX]
            IDX += 1
            CTR_1 += 1
        else:
            if T_STR in SUB_STRING:
                pass
            else:
                SUB_STRING.append(T_STR)
            CTR_2 += 1
            CTR_1 = 0
            IDX = CTR
            T_STR = ''
            if CTR_2 == CTR_N+1:
                CTR_1 = 0
                IDX += 1
                CTR += 1
                CTR_2 = CTR_1 + 1
                if CTR > 1:
                    CTR_N -= 1
        if CTR_N == 0:
            SUB_STRING.append(STRING)
            break
    COMPARE = "aeiou"
    OUTPUT = 0
    for lp_x in SUB_STRING:
        for lp_vow in COMPARE:
            if lp_vow in lp_x:
                OUTPUT += 1
    print(OUTPUT)
