import sys,collections
input = sys.stdin.readline
board = [list(input().strip()) for _ in range(12)]
dx,dy = [0,-1,0,1],[1,0,-1,0]

def bfs(x,y,color) :
  visited[x][y] = True
  q = collections.deque([[x,y]])
  deleteQ = [(x,y)]
  counting = 0
  global flag,cnt
  while q :
    cx,cy = q.popleft()
    counting += 1
    for i in range(4) :
      nx,ny = cx + dx[i], cy + dy[i]
      if 0<= nx < 12 and 0 <= ny < 6 and board[nx][ny] == color and not visited[nx][ny]:
        visited[nx][ny] = True
        q.append([nx,ny])
        deleteQ.append((nx,ny))

  if counting >= 4 :
    for x,y in deleteQ :
      board[x][y] = '.'
    flag = True
cnt = 0

def down() :
  for j in range(6) :
    for i in range(10,-1,-1) :
      if board[i][j] != '.' and board[i+1][j] == '.':
        k = i
        while k< 11 and board[k+1][j] == '.'  :
          board[k+1][j] = board[k][j]
          board[k][j] = '.'
          k += 1
          

while True :
  visited = [[False] * 6 for _ in range(12)]
  flag = False
  for i in range(12) :
    for j in range(6) :
      if board[i][j] != '.' and not visited[i][j] :
        bfs(i,j,board[i][j])
  
  if flag :
    cnt += 1
    down()
  else :
    print(cnt)
    break