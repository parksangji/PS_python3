import sys; input = sys.stdin.readline
n,m = map(int,input().split())

memory = [0] + list(map(int,input().split()))
cost = [0] + list(map(int,input().split()))
costSum = sum(cost)
dp = [[0 for _ in range(costSum+1)] for _ in range(n+1)]

for i in range(1,n+1) :
  for j in range(1,costSum + 1) :
    if j - cost[i] >= 0 :
      dp[i][j] = max(dp[i-1][j-cost[i]] + memory[i],dp[i-1][j])
    else :
      dp[i][j] = dp[i-1][j]

for i in range(costSum + 1) :
  if dp[n][i] >= m :
    print(i)
    break