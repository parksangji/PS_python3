import sys ; from collections import deque
r1,c1 = map(int,sys.stdin.readline().split()) ; r2,c2 = map(int,sys.stdin.readline().split())
dx = [-3,-2,2,3,3,2,-2,-3]
dy = [2,3,3,2,-2,-3,-3,-2]
d = {
  0 : ((-2,1),(-1,0)),
  1 : ((-1,2),(0,1)),
  2 : ((1,2),(0,1)),
  3 : ((2,1),(1,0)),
  4 : ((2,-1),(1,0)),
  5 : ((1,-2),(0,-1)),
  6 : ((-1,-2),(0,-1)),
  7 : ((-2,-1),(-1,0)),
}
def outRange(x,y) :
  if 0 <= x <= 9 and 0 <= y <= 8 :
      return False
  return True
def bfs() :
  board = [[0] * 9 for _ in range(10)]
  q = deque()
  q.append([r1,c1])
  board[r1][c1] = 0
  while q :
    x,y = q.popleft()
    for i in range(8) :
      nx = x + dx[i]
      ny = y + dy[i]
      if outRange(nx,ny) or board[nx][ny]:
        continue
      flag = False
      for xx,yy in d[i] :
        if x + xx == r2 and y + yy == c2 :
          flag = True
          break
      if flag :
        continue
      if nx == r2 and ny == c2 :
        return board[x][y] + 1
      board[nx][ny] = board[x][y] + 1
      q.append([nx,ny])
  return -1
print(bfs())