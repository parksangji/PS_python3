import sys
import heapq
input = sys.stdin.readline

arr = sorted([int(input()) for _ in range(int(input()))])
answer = 0
while len(arr) > 1 :
  a = heapq.heappop(arr) 
  b = heapq.heappop(arr)
  answer += (a+b)
  heapq.heappush(arr,a+b)
print(answer)