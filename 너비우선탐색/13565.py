import sys
from collections import deque

r,c = map(int,sys.stdin.readline().split())

arr = [list(map(int,sys.stdin.readline().strip())) for _ in range(r)]

visited = [[False] * c for _ in range(r)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(xx,yy) :
  global visited
  q = deque()
  q.append([xx,yy])
  visited[xx][yy] = True
  while q :
    x,y = q.popleft()

    if x == (r-1) :
      return True

    for i in range(4) :
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < r and 0 <= ny < c :
        if not visited[nx][ny] and arr[nx][ny] == 0 :
          visited[nx][ny] = True
          q.append([nx,ny])
  return False  
flag = False

for i in range(c) :
  if visited[0][i] == 0 and bfs(0,i):
    flag = True
    break

if flag :
  print("YES")
else :
  print("NO")