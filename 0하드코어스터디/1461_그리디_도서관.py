import sys,heapq; n,m = map(int,sys.stdin.readline().split())
under = []; up = []
for i in sorted(list(map(int,sys.stdin.readline().split()))) :
  if i < 0 :
    under.append(i)
  else :
    up.append(i)
up.sort(reverse = True)
distance = sorted([abs(under[i]) for i in range(len(under)) if i % m == 0] + [abs(up[i]) for i in range(len(up)) if i % m == 0])
print(sum(distance[:-1]) * 2 + distance[-1])