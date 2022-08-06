import sys
n,m = map(int,sys.stdin.readline().split())
know = set(list(map(int,sys.stdin.readline().split()))[1:]) 
parties = [set(list(map(int,sys.stdin.readline().split()))[1:]) for _ in range(m)]

for _ in range(m) :
  for party in parties :
    if party & know :
      know = know.union(party)
answer = 0
for party in parties :
  if party & know :
    continue
  answer += 1
print(answer)
