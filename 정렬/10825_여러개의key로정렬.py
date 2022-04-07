import sys

n = int(sys.stdin.readline())

table = list(sys.stdin.readline().split() for _ in range(n))

table.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(n) :
  print(table[i][0])