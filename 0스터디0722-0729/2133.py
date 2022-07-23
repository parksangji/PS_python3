n =  int(input())
if not n % 2:
  dp = [1,0,3,0,11] + [0] * (n+1)
  if n == [0,2,4] : print(dp[n])
  else :
    for i in range(6,n+1,2) :
      for j in range(0,i-2,2) :
        dp[i] += dp[j] * 2
      dp[i] += dp[i-2] * dp[2]
    print(dp[n])
else :
  print(0)