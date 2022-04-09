import sys
from collections import deque
input = sys.stdin.readline
n,m,k = map(int,input().split())
arr = [list(map(int,input().strip()))for _ in range(n)]
visited = [[[False] * (k+1) for _ in range(m)] for _ in range(n)]
visited[0][0] = [True] * (k+1)
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs() :
  q = deque()
  q.append([0,0,0,1])
  while q :
    x,y,attack,cnt = q.popleft()
    if x == (n-1) and y == (m-1) :
      return cnt
    for i in range(4) :
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][attack]:
        
        if arr[nx][ny] == 0:
          visited[nx][ny][attack] = True
          q.append([nx,ny,attack,cnt+1])

        elif attack < k and not visited[nx][ny][attack+1]:
          visited[nx][ny][attack+1] = True
          q.append([nx,ny,attack+1,cnt+1])
  return -1  
    
print(bfs())    