import sys,heapq;
n,m = map(int,sys.stdin.readline().split())
degree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m) :
  a,b = map(int,sys.stdin.readline().split())
  degree[b] += 1
  graph[a].append(b)
q= []

for i in range(1,n+1) :
  if degree[i] == 0 :
    heapq.heappush(q,i)
    
answer = []

while q :
  cur = heapq.heappop(q)
  for next in graph[cur] :
    degree[next] -= 1
    if degree[next] == 0 :
      heapq.heappush(q,next)
  answer.append(cur)

for i in answer :
  print(i, end = " ")