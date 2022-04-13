# 골드 5 - 무한 수열
import sys
import time

n,p,q = map(int,sys.stdin.readline().split())
dp = dict()
dp[0] = 1

def dfs(cur) :
  if cur == 0 :
    return 1
  if cur in dp :
    return dp[cur]
  else :
    dp[cur] = dfs(cur//p) + dfs(cur//q)
    return dp[cur]
dfs(n)
print(dp[n])