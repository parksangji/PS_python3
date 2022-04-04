
        
def bfs(visited,arr,xx,yy,n,m) :
  queue = []
  visited[xx][yy] = True
  queue.append([xx,yy])
  dx = [-1,-1,-1,0,1,1,1,0]
  dy = [-1,0,1,1,1,0,-1,-1]
  while queue :
    x,y = queue.pop(0)

    for i in range(8) :
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == 1:
        visited[nx][ny] = True
        queue.append([nx,ny])

  return
  
while True :
  a,b = map(int,input().split())
  if a == 0 and b == 0 :
    break
  arr = [list(map(int,input().split())) for _ in range(b)]

  visited = [[False] * a for _ in range(b)]
  cnt = 0
  for i in range(b) :
    for j in range(a) :
      if not visited[i][j] and arr[i][j] == 1 :
        bfs(visited,arr,i,j,b,a)
        cnt += 1
  print(cnt)