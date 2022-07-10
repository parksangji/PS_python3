import sys;from collections import deque ; input = sys.stdin.readline
def bfs(x,y,color) :
  q = deque([[x,y]]) ; 
  block = [[x,y]]
  rainbow = []

  while q :
    cx,cy = q.popleft()
    for i in range(4) :
      nx = cx + dx[i]
      ny = cy + dy[i]
      if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] != -1:
        if board[nx][ny] == 0 :
          rainbow.append([nx,ny])
          q.append([nx,ny])
          block.append([nx,ny])
          visited[nx][ny] = True
        if board[nx][ny] == color :
          q.append([nx,ny])
          block.append([nx,ny])
          visited[nx][ny] = True

  for i,j in rainbow :
    visited[i][j] = False
  return block,rainbow

def grabity(board) :
  for i in range(n-2,-1,-1) :
    for j in range(n) :
      if board[i][j] > -1 :
        tmp = i
        while 1 :
          if 0<= tmp+1 < n and board[tmp+1][j] == -100 :
            board[tmp+1][j] = board[tmp][j]
            board[tmp][j] = -100
            tmp += 1
          else :
            break

def rotate(board) :
  tmpBoard = []
  for i in range(n-1,-1,-1) :
    tmp = []
    for j in range(n) :
      tmp.append(board[j][i])
    tmpBoard.append(tmp)
  return tmpBoard

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
dx = [0,0,-1,1] ; dy = [-1,1,0,0]
answer = 0

while True :
  delBlock = []
  visited = [[False] * n for _ in range(n)]
  ### 1st job
  
  for i in range(n) :
    for j in range(n) :
      if board[i][j] > 0 and not visited[i][j] :
        visited[i][j] = True
        block,rainbow  = bfs(i,j,board[i][j])
        size= len(block)
        rainsize = len(rainbow)
        if size >= 2 :
          delBlock.append([size,rainsize,block])
  if not delBlock :
    break
  delBlock.sort(reverse = True)

  answer += (delBlock[0][0] **2)
  
  ### 2nd jobx
  for i,j in delBlock[0][2] :
    board[i][j] = -100
  ### 3th job
  grabity(board)
  
  ### 4th
  board = rotate(board)

  ### 5th
  grabity(board)
print(answer)