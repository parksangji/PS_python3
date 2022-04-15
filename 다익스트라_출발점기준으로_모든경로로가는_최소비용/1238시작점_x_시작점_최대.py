import sys ;import heapq ; input = sys.stdin.readline
n,m,x = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m) :
  a,b,t = map(int,input().split())
  graph[a].append((b,t))

def dijkstra(start) :
  dist = [sys.maxsize] * (n+1)
  dist[start] = 0
  q = []
  heapq.heappush(q,(0,start))
  while q :
    weight,cur = heapq.heappop(q)

    if dist[cur] < weight :
      continue
    for next,cost in graph[cur] :
      if weight+cost < dist[next] :
        dist[next] = weight + cost 
        heapq.heappush(q,(weight+cost,next))
  return dist
from_ = dijkstra(x) 
answer = 0
for i in range(1,n+1):
  if i == x :
    continue
  answer = max(dijkstra(i)[x] + from_[i],answer)
print(answer)