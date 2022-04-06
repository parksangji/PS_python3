import sys
from itertools import permutations

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
b = list(permutations(a,n))

sum = 0

for i in b :
  tmp = 0
  for j in range(n-1) :
    tmp += abs(i[j] - i[j+1])
  sum = max(tmp,sum)
print(sum)

"""
from itertools import*;input();
print(max(sum(abs(a-b)for a,b in zip(c,c[1:]))for c in permutations(map(int,input().split()))))

"""