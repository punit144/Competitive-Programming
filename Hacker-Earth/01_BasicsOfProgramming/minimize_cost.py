"""
    Author: Punit Grewal
    Year: 2019
    Github: https://github.com/punit144/Competitive-Programming
    Problem: HackerEarth < Basics of Programming Input
    Complexity: Medium
"""
def min_val(k_val, arr):
    """ Calculate min value of Cx"""
    compute = 0
    ctr = 0
    z_ctr = k_val
    for i in arr:

        if i >= 0:
            ctr += 1
            compute += i
            z_ctr = k_val
        elif ctr == 0:
            return abs(sum(arr) + i)
        else:
            z_ctr += -1
            if z_ctr < 0:
                compute += abs(i)
            else:
                compute += i
    return abs(compute)

N, K = list(map(int, input().split()))
ARR = list(map(int, input().split()))
MIN_VALUE = min_val(K, ARR)
print(MIN_VALUE)
