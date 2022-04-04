import sys
n = int(input())
arr = list(list(map(int,sys.stdin.readline().split())) for _ in range(n))
dp = [0] * (n+1)
for i in range(n-1,-1,-1) :
  t,p = arr[i]
  if i + t > n :
    dp[i] = dp[i+1]
  else :
    dp[i] = max(dp[i+1],dp[i+t] +p)
print(dp[0])

"""
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
"""