import sys

n = int(sys.stdin.readline())
dist = [0] + list(map(int,sys.stdin.readline().split())) + [0]
price = list(map(int,sys.stdin.readline().split()))

compare = price[0]
total = dist[1] * compare 

for i in range(1,n) :
  if compare < price[i] :
    total += compare * dist[i+1]
  else :
    compare = price[i]
    total += compare * dist[i+1]

print(total)