from sys import stdin
n = int(stdin.readline())

dp = [0 for _ in range(n+1)]
sqr = [ i*i for i in range(1,n+1) ]


for i in range(1,n+1) :

  tmp = []  
  for j in sqr :
    if j > i :
      break
    tmp.append(dp[i-j])

  dp[i] = min(tmp) + 1
print(dp[n])

