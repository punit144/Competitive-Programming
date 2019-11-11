"""
    Author: Punit Grewal
    Year: 2019
    Github: https://github.com/punit144/Competitive-Programming
    Problem: HackerEarth <
    Complexity:
"""
def permute(arrA, arrB):
    str_dic = {}
    length = len(arrA)
    for lp_f1 in arrA:
        if lp_f1 in str_dic:
            str_dic[lp_f1] += 1
        else:
            str_dic[lp_f1] = 0
    for lp_f2 in arrB:
        if lp_f2 in str_dic:
            str_dic[lp_f2] -= 1
        else:
            return("No")
    if str_dic.values <= 0:
        return("No")
    else:
        return("Yes")


TEST = int(input())
for lp_1 in range(TEST):
    ARR_STR = list(map(str, input().split()))
    permute(ARR_STR[0], ARR_STR[1])




