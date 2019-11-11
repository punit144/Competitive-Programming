"""
    Author: Punit Grewal
    GitHub: https://github.com/punit144/Code-Monk
"""
TOTAL_SEAT = {}
for i in range(1, 109, 12):
    TOTAL_SEAT[i] = i+11, 'WS'
    TOTAL_SEAT[i+1] = i+1+9, 'MS'
    TOTAL_SEAT[i+2] = i+2+7, 'AS'
    TOTAL_SEAT[i+3] = i+3+5, 'AS'
    TOTAL_SEAT[i+4] = i+4+3, 'MS'
    TOTAL_SEAT[i+5] = i+5+1, 'WS'
    TOTAL_SEAT[i+6] = i+6-1, 'WS'
    TOTAL_SEAT[i+7] = i+7-3, 'MS'
    TOTAL_SEAT[i+8] = i+8-5, 'AS'
    TOTAL_SEAT[i+9] = i+9-7, 'AS'
    TOTAL_SEAT[i+10] = i+10-9, 'MS'
    TOTAL_SEAT[i+11] = i+11-11, 'WS'
# print(TOTAL_SEATS, sep="\n")
TEST_COUNT = input()
TEST_INPUT = []
for j in range(int(TEST_COUNT)):
    TEST_INPUT.append(int(input()))

# print(TEST_INPUT)
LENGTH_INPUT = len(TEST_INPUT)
for k in range(LENGTH_INPUT):
    val_1, val2 = TOTAL_SEAT[TEST_INPUT[k]]
    print(val_1, val2)
