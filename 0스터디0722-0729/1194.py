from collections import deque

n,m = map(int,input().split())
board = [list(input().strip()) for _ in range(n)]

start = None

for i in range(n) :
  if start != None : break
  for j in range(m) :
    if board[i][j] == "0" : 
      board[i][j] = '.'
      start = (i,j)

def bfs() :
  x,y = start
  q = deque([(x,y,0,0)])
  visited = [[[0] * 64 for _ in range(m)] for _ in range(n)]
  dx,dy = [0,0,-1,1],[-1,1,0,0]
  visited[x][y][0] = True
  while q :
    x,y,cnt,key = q.popleft()
    if board[x][y] == "1" :
      return cnt
    else :
      for i in range(4) :
        nx,ny = x + dx[i],y + dy[i]
        if 0 <= nx < n and 0<= ny < m and board[nx][ny] != '#' and not visited[nx][ny][key] :
          if board[nx][ny] == '.' :
            visited[nx][ny][key] = True
            q.append((nx,ny,cnt+1,key))
          elif board[nx][ny] == "1" :
            return cnt+1
          elif board[nx][ny] in "ABCDEF" and key & 1 << (ord(board[nx][ny])- 65):
            visited[nx][ny][key] = True
            q.append((nx,ny,cnt+1,key))
          elif board[nx][ny] in "abcdef" and not visited[nx][ny][key|(1 << ord(board[nx][ny]) - 97)] :
            visited[nx][ny][key | (1 << ord(board[nx][ny]) - 97)] = True
            q.append((nx,ny,cnt+1,key | (1 << ord(board[nx][ny]) - 97)))
  return -1
print(bfs())