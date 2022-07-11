import sys,itertools,collections
input = sys.stdin.readline
arr = [[list(map(int,input().split())) for _ in range(5)] for _ in range(5)]
dx,dy,dz = [0,0,0,1,0,-1],[0,0,1,0,-1,0],[1,-1,0,0,0,0]
ans = sys.maxsize

def bfs() :
  global ans
  visited = [[[0] * 5 for _ in range(5)] for _ in range(5)]
  visited[0][0][0] = 0
  q = collections.deque([(0,0,0)])
  while q :
    x,y,z = q.popleft()
    if visited[x][y][z] >= ans :
      continue
    if x == 4 and y == 4 and z == 4 :
      ans = min(ans,visited[4][4][4])
      if ans == 12 :
        print(12) 
        exit(0)
      return
    for i in range(6) :
      nx,ny,nz = x + dx[i],y + dy[i], z + dz[i]
      if 0 <= nx < 5 and 0<= ny < 5 and 0<= nz < 5 and visited[nz][nx][ny] == 0 and board[nz][nx][ny] :
        visited[nz][nx][ny] = visited[z][x][y] + 1
        q.append((nx,ny,nz))
  return

def dfs(idx) :
  if idx == 5 :
    if board[4][4][4] : bfs() 
    return
  for i in range(4) :
    if board[0][0][0] : dfs(idx+1)
    board[idx] = [list(reversed(i)) for i in zip(*board[idx])]
  
for i in itertools.permutations([0,1,2,3,4]) :
  board = [arr[ii] for ii in i]
  dfs(0)
print(ans if ans != sys.maxsize else -1)