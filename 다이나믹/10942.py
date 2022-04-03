import sys
n = int(input())
arr = list(map(int,sys.stdin.readline().split()))
m = int(input())
dp = [[0] * n for _ in range(n)]

for nn in range(n) :
  for start in range(n- nn) :
    end = start + nn
    if start == end :
      dp[start][end] = 1
    elif arr[start] == arr[end] :
      if start +1 == end :
        dp[start][end] = 1
      elif dp[start+1][end-1] == 1 :
        dp[start][end] = 1

while m :
  a,b = map(int,sys.stdin.readline().split())
  print(dp[a-1][b-1])
  m -=1  