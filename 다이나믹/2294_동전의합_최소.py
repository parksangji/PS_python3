n,k = map(int,input().split())
arr = [int(input()) for _ in range(n)]
dp = [100001] * (k+1)
dp[0] = 0

for i in range(n) :
  for j in range(arr[i],k+1) :
    dp[j] = min(dp[j] , dp[j- arr[i]] + 1)
    
print(dp[k] if dp[k] != 100001 else -1)