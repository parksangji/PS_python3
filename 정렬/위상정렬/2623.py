import sys;from collections import deque ;input =sys.stdin.readline
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
degree = [0] * (n+1)
for _ in range(m) :
  tmp = list(map(int,input().split()))
  for i in range(2,len(tmp)) :
    degree[tmp[i]] += 1
    graph[tmp[i-1]].append(tmp[i])
q = deque()
result = []
for i in range(1,n+1) :
  if degree[i] == 0 :
    q.append(i)
while q :
  cur = q.popleft()
  result.append(cur)
  for next in graph[cur] :
    degree[next] -= 1
    if degree[next] == 0:
      q.append(next)
if len(result) == n :
  for i in result :
    print(i)
else :
  print(0)