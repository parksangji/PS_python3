mport sys
from collections import deque

n = int(input())

r1,c1,r2,c2 = map(int,sys.stdin.readline().split())
visited = [[False] * n for _ in range(n)]
dx = [-2,-2,0,0,2,2]
dy = [-1,+1,-2,2,-1,1]

def bfs():
  dq = deque()
  dq.append((r1,c1,0))
  visited[r1][c1] = True
  while dq :
    x,y,cnt = dq.popleft()
  
    if x == r2 and y == c2 :
      return cnt
    
    for i in range(6) :
      nx = x + dx[i]
      ny = y + dy[i]
  
      if nx < 0 or ny < 0 or nx >= n or ny >= n :
        continue
      if visited[nx][ny] :
        continue
      visited[nx][ny] = True
      dq.append((nx,ny,cnt+1))
  return -1
print(bfs())