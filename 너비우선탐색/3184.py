import sys

r,c = map(int,sys.stdin.readline().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x,y) :
  q = [[x,y]]
  visited[x][y] = 1
  v = 0 ; o = 0
  while q :
    xx,yy = q.pop(0)
    if arr[xx][yy] == 'v' :
      v += 1
    elif arr[xx][yy] == 'o' :
      o += 1
    for i in range(4) :
      nx = xx + dx[i]
      ny = yy + dy[i]
      if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == 0:
        if arr[nx][ny] == '#' :
          continue
        q.append([nx,ny])
        visited[nx][ny] = 1
  return v,o

a = 0 ;b = 0

for i in range(r) :
  for j in range(c) :
    if arr[i][j] == '#' :
      continue
    elif visited[i][j] == False:
      wolf,sheep = bfs(i,j)
      if wolf < sheep :
        a += sheep
      else :
        b += wolf
print(a,b)