import sys
from itertools import *

n = int(sys.stdin.readline())

arr = list(permutations([i for i in range(1,n+1)],n))

for i in range(len(arr)) :
  for j in range(n) :
    print(arr[i][j],end = " ")
  print()