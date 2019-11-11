"""
    Author: Punit Grewal
    Year: 2019
    Github: https://github.com/punit144/Competitive-Programming
    Problem: HackerEarth <
    Complexity:
"""


def permute(arrA, arrB):
    str_dic = {}
    value = True
    for lp_f1 in arrA:
        if lp_f1 in str_dic:
            str_dic[lp_f1] += 1
        else:
            str_dic[lp_f1] = 1
    for lp_f2 in arrB:
        if lp_f2 in str_dic:
            str_dic[lp_f2] -= 1
        else:
            pass
            # value = False
    for str_val in str_dic.values():
        if str_val <= 0:
            continue
        else:
            value = False
    if value:
        print("Yes")
    else:
        print("No")


TEST = int(input())
for lp_1 in range(TEST):
    ARR_STR = list(map(str, input().split()))
    permute(ARR_STR[0], ARR_STR[1])
