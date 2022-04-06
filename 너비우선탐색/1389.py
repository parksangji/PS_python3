import sys

n,m = map(int,sys.stdin.readline().split())

arr = [[] for _ in range(n+1)]
for i in range(m) :
  a,b = map(int,sys.stdin.readline().split())
  arr[a].append(b)
  arr[b].append(a)

def bfs(start,end) :
  visited = [False for _ in range(n+1)] 
  q = [[start,0]]
  visited[start] = True

  while q :
    cur,cnt = q.pop(0)
    if cur == end :
      return cnt
    for next in arr[cur] :
      if not visited[next] :
        q.append([next,cnt+1])
        visited[next] = True
  
  return 0
  
answer = 987654321
idx = 0

for i in range(1,n+1) :
  sum = 0
  for j in range(1,n+1) :
    if i != j : 
      sum += bfs(i,j)
  if sum < answer :
    answer = sum
    idx = i
print(idx)
