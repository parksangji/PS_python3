n = int(input())
a,b = map(int,input().split())
m = int(input())

arr = [[] for _ in range(n+1)]
for i in range(m) :
  x,y = map(int,input().split())
  arr[x].append(y)
  arr[y].append(x)

def bfs() :
  q = [[a,0]]
  visited = [False] * (n+1)
  visited[a] = True
  while q :
    cur,cnt = q.pop(0)
    if cur == b :
      return cnt
      break
    for next in arr[cur] :
      if not visited[next] :
        visited[next] = True
        q.append([next,cnt+1])
  return -1

print(bfs())