import sys

n,m = map(int,sys.stdin.readline().split())

arr = [[p for p in sys.stdin.readline().strip()] for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = False

def dfs(x,y,xx,yy,color,depth) :
  global ans
  for i in range(4) :
    if ans is True :
      return
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or ny < 0 or nx >=n or ny >= m :
      continue
    if depth >= 4 and xx == nx and yy == ny :
      ans = True
      return True
    
    if visited[nx][ny] == 0 and arr[nx][ny] == color :
      visited[nx][ny] = 1
      dfs(nx,ny,xx,yy,color,depth+1)
      visited[nx][ny] = 0
  return False
def solve() :
  for i in range(n) :
    for j in range(m) :
      if not visited[i][j] :
        visited[i][j] = True
        dfs(i,j,i,j,arr[i][j],1)

        if ans :
          return 'Yes'
  return 'No'
print(solve())