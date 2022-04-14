import sys
n = int(input())
hash = {}
for _ in range(n) :
  compare = int(sys.stdin.readline())
  if compare in hash :
    hash[compare] += 1
  else :
    hash[compare] = 1
print(sorted(hash.items(),key = lambda x : [-x[1],x[0]])[0][0])