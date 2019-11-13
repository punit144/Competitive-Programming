"""
    Author: Punit Grewal
    Year: 2019
    Github: https://github.com/punit144/Competitive-Programming
    Problem: HackerEarth <
    Complexity:
"""
TEST = int(input())
for lp_g1 in range(TEST):
    DTR = 5
    INPUT = int(input())
    OUTPUT_1 = 1
    while DTR < INPUT:
        OUTPUT_1 += DTR
        DTR = DTR*5
    if DTR > 5:
        DTR = DTR // 5
        OUTPUT_1 -= DTR
    OUTPUT = ((DTR*INPUT)//(OUTPUT_1))
    if (DTR*INPUT) % OUTPUT_1 > 0:
        OUTPUT += 5
    if OUTPUT % 5 or OUTPUT % 2 == 0:
        print("5")
        for lp_g2 in range(5):
            print(OUTPUT, end=' ')
            OUTPUT += 1
    else:
        print("0", end='')
    # for lp_g2 in range(5):
    #    print(OUTPUT, sep=" ", end=" ")
    #    OUTPUT += 1
    print()
