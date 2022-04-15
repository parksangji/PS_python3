import sys
import heapq
n,e = map(int,sys.stdin.readline().split())
arr = [[] for _ in range(n+1)]

for _ in range(e) :
  a,b,c = map(int,sys.stdin.readline().split())
  arr[a].append((b,c))
  arr[b].append((a,c))
v1,v2 = map(int,sys.stdin.readline().split())

def dijkstra(start) :
  dist = [float('inf')] * (n+1)
  q = []
  heapq.heappush(q,(0,start))
  dist[start] = 0
  while q :
    cost,cur = heapq.heappop(q)
    if dist[cur] < cost :
      continue
    for next,w in arr[cur] :
      weight = cost + w
      if weight < dist[next] :
        dist[next] = weight
        heapq.heappush(q,(weight,next))
  return dist

a = dijkstra(1)
b = dijkstra(v1)
c = dijkstra(v2)
answer = min(a[v1] + b[v2] + c[n],a[v2] + c[v1]  +b[n])
if answer >= float('inf') :
  print(-1)
else :
  print(answer)
  