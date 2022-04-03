import sys

t = int(input())

def solve(n) :
  arr = []
  for _ in range(n) :
    a,b = map(int,sys.stdin.readline().split())
    arr.append([a,b])

  arr.sort()
  cnt = 1
  compare = arr[0][1]

  for i in range(1,n) :
    if compare > arr[i][1] :
      cnt += 1
      compare = arr[i][1]
  return cnt


for _ in range(t) :
  n = int(input())
  print(solve(n))
    
    