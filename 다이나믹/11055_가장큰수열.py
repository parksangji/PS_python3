n = int(input())

arr = list(map(int,input().split()))

dp = [0] * n
answer = 0
for i in range(n) :
  dp[i] = arr[i]
  for j in range(i) :
    if arr[j] < arr[i] and dp[i] < dp[j] + arr[i] :
      dp[i] = dp[j] + arr[i]
  answer = max(dp[i],answer)
  
print(dp)