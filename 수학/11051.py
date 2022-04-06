import sys
n,k = map(int,sys.stdin.readline().split())

up = 1; down = 1

while k :
  up *= n;down *= k
  n -= 1;k -= 1

print((up // down) % 10007)