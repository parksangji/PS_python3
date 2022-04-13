# 골드 3 - 과제
import sys
import heapq

input = sys.stdin.readline
n = int(input())
arr = []
dp = [0] * 1001

for i in range(n) :
  day,value = map(int,input().split())
  arr.append([-value,day,value])
  
heapq.heapify(arr)
while arr :
  tmp = heapq.heappop(arr)
  for i in range(tmp[1],0,-1) :
    if dp[i] == 0 :
      dp[i] = tmp[-1]
      break
print(sum(dp))