import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
if sum(arr) % 4:
    print(0)
else:
    cnt = [0]*4 ; cnt[0] = 1 
    pSum = 0
    division = sum(arr)//4
    for i in range(n-1):
        pSum += arr[i]
        if pSum == 3*division :
            cnt[3] += cnt[2]
        if pSum == 2*division :
            cnt[2] += cnt[1]
        if pSum == 1*division :
            cnt[1] += cnt[0]
    print(cnt[3])