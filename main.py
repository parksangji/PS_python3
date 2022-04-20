import sys; from collections import deque

def init(r,c) :
  red = [] ; blue = [] ; board = []
  for i in range(r) :
    tmp = list(sys.stdin.readline().strip())
    for j in range(c) :
      if tmp[j] == 'R' :
        red = [i,j]
      if tmp[j] == 'B' :
        blue = [i,j]
    board.append(tmp)
  return board,red,blue

def move(x,y,i,c) :
  while arr[x+dx[i]][y+dy[i]] != '#' and arr[x][y] != 'O' :
    x += dx[i]
    y += dy[i]
    c += 1
  return x,y,c

def bfs() :
  q = deque()
  q.append([red[0],red[1],blue[0],blue[1],0])
  visited = {str(red[0]) + str(red[1]) + str(blue[0]) + str(blue[1]) : True}
  while q :
    rx,ry,bx,by,cnt = q.popleft()
    if cnt >= 10 :
      break
    for i in range(4) :
      nrx,nry,rc = move(rx,ry,i,0)
      nbx,nby,bc = move(bx,by,i,0)
      if arr[nbx][nby] == 'O' :
        continue
      if arr[nrx][nry] == 'O' :
        return cnt + 1
      if nrx == nbx and nry == nby :
        if rc > bc :
          nrx -= dx[i]
          nry -= dy[i]
        else :
          nbx -= dx[i]
          nby -= dy[i]
      route = str(nrx) + str(nry) + str(nbx) + str(nby)
      if route in visited :
        continue
      visited[route] = True
      q.append([nrx,nry,nbx,nby,cnt+1])
  return -1

n,m = map(int,sys.stdin.readline().split())
arr,red,blue = init(n,m)
arr[red[0]][red[1]] = '.'
arr[blue[0]][blue[1]] = '.'
dx = [0,0,-1,1]
dy = [1,-1,0,0]
print(bfs())