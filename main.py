import sys
input = sys.stdin.readline

n,l = map(int,input().split())

for i in range(l,101) :
  x = n - (i * (i+1) / 2)
  if x % i == 0 and x // i >= -1 :
    for j in range(1,i+1) :
      print(int(x//i + j), end = " ")
    break
else :
  print(-1)