import sys; input = sys.stdin.readline
n,k = map(int,input().split())
coin = [int(input()) for _ in range(n)]
dp = [0] + [sys.maxsize] * (k)

for i in range(n) :
  for j in range(coin[i],k+1) :
    dp[j] = min(dp[j],dp[j-coin[i]] + 1)
print(dp[k] if dp[k] != sys.maxsize else -1)