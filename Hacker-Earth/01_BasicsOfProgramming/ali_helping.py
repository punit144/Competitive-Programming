"""
    Author: Punit Grewal
    Year: 2019
    Github: https://github.com/punit144/Competitive-Programming
    Problem: HackerEarth <
    Complexity:
"""
STRING = str(input())
ARR = []
for lp_1 in STRING:
    ARR.append(lp_1)

CMP_1 = int(ARR[0]) + int(ARR[1])
CMP_2 = int(ARR[3]) + int(ARR[4])
CMP_3 = int(ARR[4]) + int(ARR[5])
CMP_4 = ARR[2]
CMP_5 = int(ARR[7]) + int(ARR[8])
OUTPUT = []

if CMP_1 % 2 == 0:
    OUTPUT.append(True)
else:
    OUTPUT.append(False)
if CMP_2 % 2 == 0:
    OUTPUT.append(True)
else:
    OUTPUT.append(False)
if CMP_3 % 2 == 0:
    OUTPUT.append(True)
else:
    OUTPUT.append(False)
if CMP_5 % 2 == 0:
    OUTPUT.append(True)
else:
    OUTPUT.append(False)
if CMP_4 not in "AEIOUY":
    OUTPUT.append(True)
else:
    OUTPUT.append(False)
VALUE = 1
for lp_3 in OUTPUT:
    if lp_3 is False:
        VALUE = 0
if VALUE:
    print("valid")
else:
    print("invalid")

