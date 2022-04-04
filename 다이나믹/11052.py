n = int(input())

p = [0] + list(map(int,input().split()))
dp = [0] * (n+1)

for i in range(1,n+1) :
  for j in range(1,i+1) :
    dp[i] = max(dp[i-j] + p[j],dp[i])

print(dp[n])

""" 3장을 구매할때 최대 금액
p[1] + dp[2] | 카드 한장 가격 + 2장의 카드를 구매하는데 최대 금액
p[2] + dp[1]

p[3] + dp[0]
"""