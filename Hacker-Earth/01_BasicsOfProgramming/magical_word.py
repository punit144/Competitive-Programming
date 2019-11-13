"""
    Author: Punit Grewal
    Year: 2019
    Github: https://github.com/punit144/Competitive-Programming
    Problem: HackerEarth <
    Complexity:
"""
TEST = int(input())
for lp_fn in range(TEST):
    VAR_1 = 0
    OUTPUT = ''
    N = int(input())
    STRING = str(input())
    for lp_g2 in STRING:
        VAR_1 = ord(lp_g2)
        if VAR_1 < 65:
            OUTPUT += "C"
        elif 65 <= VAR_1 <= 69:
            OUTPUT += "C"
        elif 70 <= VAR_1 <= 72:
            OUTPUT += "G"
        elif 73 <= VAR_1 <= 76:
            OUTPUT += "I"
        elif 77 <= VAR_1 <= 81:
            OUTPUT += "O"
        elif 82 <= VAR_1 <= 86:
            OUTPUT += "S"
        elif 87 <= VAR_1 <= 90:
            OUTPUT += "Y"
        elif 91 <= VAR_1 <= 93:
            OUTPUT += "Y"
        elif 94 <= VAR_1 <= 99:
            OUTPUT += "a"
        elif 100 <= VAR_1 <= 102:
            OUTPUT += "e"
        elif 103 <= VAR_1 <= 105:
            OUTPUT += "g"
        elif 106 <= VAR_1 <= 108:
            OUTPUT += "k"
        elif 109 <= VAR_1 <= 111:
            OUTPUT += "m"
        else:
            OUTPUT += "q"
    print(OUTPUT)

