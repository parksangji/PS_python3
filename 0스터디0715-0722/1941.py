from collections import deque
def bfs(x=0,y=0) :
  matrix = [[False for _ in range(5)]  for _ in range(5)]
  connect = [[False for _ in range(5)]  for _ in range(5)]
  for i in range(25) :
    if not visited[i] : continue
    x,y = i//5, i% 5
    matrix[x][y] = True
  q = deque([(x,y)])
  connect[x][y] = True
  cnt = 1
  while q :
    x,y = q.popleft()
    for i in range(4) :
      nx,ny = x + dx[i],y + dy[i]
      if 0<= nx < 5 and 0 <= ny < 5 and not connect[nx][ny] and matrix[nx][ny] :
        connect[nx][ny] = True
        q.append((nx,ny))
        cnt += 1
  if cnt == 7 : return True
  return False
  
def dfs(cur,depth,cntS) :
  global ans
  if depth == 7 :
    if cntS >= 4 and bfs() : ans += 1
    return
  for i in range(cur,25) :
    if visited[i] : continue
    visited[i] = True
    if arr[i//5][i%5] == "S" : 
      dfs(i,depth+1,cntS + 1)
    elif arr[i//5][i%5] == "Y" : 
      dfs(i,depth+1,cntS)
    visited[i] = False


arr = [input().strip() for _ in range(5)]
visited = [False for _ in range(25)] 
dx,dy = [0,0,-1,1],[-1,1,0,0]
ans = 0
dfs(0,0,0)
print(ans)