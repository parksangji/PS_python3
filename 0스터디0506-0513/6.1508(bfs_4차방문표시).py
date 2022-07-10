import sys,collections; input =sys.stdin.readline

def bfs() :
  q = collections.deque([[A,B,0]])
  ## A,B visited flag
  visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
  visited[A[0]][A[1]][B[0]][B[1]] = True
  while q :
    a,b,cnt = q.popleft()
    if a == B and  b == A :
      return cnt
    ax,ay =a  ; bx,by = b
    for i in range(8) :
      for j in range(8) :
        nax, nay = ax + dx[i],ay + dy[i]
        nbx, nby = bx + dx[j],by + dy[j]
        ## outRange or move to "X"
        if nax <0 or nay < 0 or nax >= n or nay >= m or board[nax][nay] == 'X' :
          continue
        if nbx <0 or nby < 0 or nbx >= n or nby >= m or board[nbx][nby] == 'X' :
          continue
        ## Route visited 
        if visited[nax][nay][nbx][nby] :
          continue
        ## dont same position 
        if nax == nbx and nay == nby :
          continue
        ## dont cross moving
        if nax == bx and nay == by and nbx == ax and nby == ay :
          continue
        ## done
        visited[nax][nay][nbx][nby] = True
        q.append([(nax,nay),(nbx,nby),cnt+1])
  return -1      

### input
n,m = map(int,input().split())
board = [list(input().strip()) for _ in range(n)]
A,B = 0,0 ; dx = [0,0,-1,1,1,-1,1,-1,0] ; dy = [1,-1,0,0,1,1,-1,-1,0]

### player find
for i in range(n) :
  for j in range(m) :
    if board[i][j] == 'A' :
      A = (i,j)
    elif board[i][j] == 'B' :
      B = (i,j)
    else :
      continue
print(bfs())