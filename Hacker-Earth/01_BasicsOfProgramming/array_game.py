"""
Author: Punit Grewal
Site: Hackearth
"""

for _ in range(int(input())):
    arr_len = int(input())
    arr = tuple(map(int, input().split()))
    maxi = [0] * arr_len
    mini = [0] * arr_len
    maxi[0] = arr[0]
    mini[arr_len-1] = arr[arr_len-1]
    ctr = 0
    for i in range(1, arr_len):
        maxi[i] = max(maxi[i-1], arr[i])
        mini[arr_len-i-1] = min(mini[arr_len-i], arr[arr_len-i-1])
    for i in range(arr_len-1):
        if maxi[i] < mini[i+1]:
            c = ctr+1
    if ctr % 2 == 1:
        print('Jeel')
    else:
        print('Ashish')
