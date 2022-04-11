import sys
import heapq

input = sys.stdin.readline

n,m = map(int,input().split())

six = []
one = []

for _ in range(m) :
  price,oneprice = map(int,input().split())
  six.append(price)
  six.append(6*oneprice)
  one.append(oneprice)
answer = 0
while n :
  if 6 < n :
    n -= 6
    answer += min(six)
  else :
    answer += min(min(six),n * min(one))
    n = 0
print(answer)