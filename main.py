import sys,collections
input = sys.stdin.readline
n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
dx,dy = [-1,1,0,0],[0,0,-1,1]
dir = [(0,-1),(1,0),(0,1),(-1,0)]

def fireball() :
  d,s = map(int,input().split())
  cnt = 0
  x = y = n//2
  while cnt < s :
    x,y = x + dx[d-1], y + dy[d-1]
    board[x][y] = 0
    cnt+=1
  rotation()
  
def rotation() :
  start = [n//2,n//2]
  q = collections.deque([])
  cnt,d,depth = 0,0,1
  x,y = start
  while 0<= x < n and 0 <= y < n :
    for _ in range(depth) :
      x,y = x + dir[d][0], y + dir[d][1]
      if board[x][y] != 0 :
        q.append(board[x][y])
    d = (d + 1) % 4
    cnt += 1
    if cnt % 2 == 0 : depth += 1
  cnt,d,depth = 0,0,1
  x,y = start
  while 0<= x < n and 0 <= y < n :
    for _ in range(depth) :
      x,y = x + dir[d][0], y + dir[d][1]
      if q : board[x][y] = q.popleft()
      else : board[x][y] = 0
    d = (d + 1) % 4
    cnt += 1
    if cnt % 2 == 0 : depth += 1

def bfs(x,y,color) :
  q = collections.deque((x,y))
  deleteQ = [(x,y)]
  

def bumb() :
  

for _ in range(m) :
  fireball()
  while bumb() :
    rotation()
  
  