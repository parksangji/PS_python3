import sys
n,m,r = map(int,sys.stdin.readline().split())
items = list(map(int,sys.stdin.readline().split()))
inf = 100000
arr = [[inf] * (n) for _ in range(n)]
for i in range(n) :
  arr[i][i] = 0

for _ in range(r) :
  a,b,l = map(int,sys.stdin.readline().split())
  arr[a-1][b-1] = l
  arr[b-1][a-1] = l

for k in range(n) :
  for i in range(n) :
    for j in range(n) :
      if arr[i][k] + arr[k][j] < arr[i][j] :
        arr[i][j] = arr[i][k] + arr[k][j]
answer = 0

for i in range(n) :
  tmp = items[i]
  for j in range(n) :
    if arr[i][j] > m or i == j:
      continue
    else :
      tmp += items[j]
  answer = max(tmp,answer)
print(answer)