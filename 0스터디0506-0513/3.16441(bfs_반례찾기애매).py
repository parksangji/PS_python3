import sys,collections;
n,m = map(int,sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [0,0,-1,1] ; dy = [-1,1,0,0]

def bfs(i,j) :
  q = collections.deque([[i,j]])
  visited[i][j] = True
  while q :
    x,y = q.popleft()
    for i in range(4) :
      nx,ny = x + dx[i], y + dy[i]

      if board[nx][ny] == "#" : continue
      if board[nx][ny] == '.' and not visited[nx][ny] :
        visited[nx][ny] = True ;q.append([nx,ny])
      if board[nx][ny] == "+" :
        while 1 :
          nx += dx[i] ; ny += dy[i]
          if board[nx][ny] == "#" :
            nx -= dx[i] ; ny -= dy[i] ;break
          elif board[nx][ny] == "." : break
          elif board[nx][ny] == "+" : continue
        if not visited[nx][ny] :
          visited[nx][ny] = True ; q.append([nx,ny])

for i in range(n) :
  for j in range(m) :
    if board[i][j] == "W" and not visited[i][j] :
      bfs(i,j)

for i in range(n) :
  for j in range(m) :
    if visited[i][j] :
      print(board[i][j] , end = "")
    else :
      if board[i][j] == '.' :
        print("P",end = "")
      else :
        print(board[i][j], end = "")
  print()