import sys
input = sys.stdin.readline

n,t = map(int,input().split())
arr = []
tele = []
dp = [[987654321] * n for _ in range(n)]
for i in range(1,n+1) :
  s,x,y = map(int,input().split())
  arr.append([x,y])   
  tele.append(s)

for i in range(n) :
  for j in range(n) :
    if i == j :
      dp[i][j] = 0
    else :
      a,aa = arr[i],tele[i]
      b,bb = arr[j],tele[j]
      dist = abs(a[0]-b[0]) + abs(a[1] - b[1])
      if aa == bb == 1 :
        dp[i][j] = min(t,dist)
      else :
        dp[i][j] = dist
for k in range(n) :
  for i in range(n) :
    for j in range(n) :
      if dp[i][k] + dp[k][j] < dp[i][j] :
        dp[i][j] = dp[i][k] + dp[k][j]
m = int(input())

for _ in range(m) :
  a,b = map(int,input().split())
  print(dp[a-1][b-1])
  
"""
6 3
0 1 2
0 5 1
1 3 3
1 1 5
0 3 5
1 7 5
5
1 2
1 5
1 6
3 4
4 2

"""