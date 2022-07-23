from collections import deque

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(m)]
visited,dx,dy = [[0] * n for _ in range(m)],[0,-1,0,1],[-1,0,1,0]
roomCntBoard = {}
roomCnt = 1
roomMaxValue = []
roomCombinationList = set()

def bfs(x,y,color) :
  visited[x][y] = color
  q = deque([(x,y)])
  boardColor = []
  while q :
    x,y = q.popleft()
    binary = bin(board[x][y])[2:]
    binary = '0' * (4-len(binary)) + binary
    b = list(map(int,binary))
    b.reverse()
    boardColor.append((x,y))
    for i in range(4) :
      nx,ny = x + dx[i],y + dy[i]
      if not b[i] and 0<= nx < m and 0<= ny < n and  not visited[nx][ny] :
        visited[nx][ny] = color
        q.append((nx,ny))
  cnt = len(boardColor)
  for x,y in boardColor :
    roomCntBoard[(x,y)] = cnt
  return cnt
  
for i in range(m) :
  for j in range(n) :
    if not visited[i][j] :
      roomMaxValue.append(bfs(i,j,roomCnt))
      roomCnt +=1

for i in range(m) :
  for j in range(n) :
    color = visited[i][j]
    for k in range(4) :
      ni,nj = i + dx[k], j + dy[k]
      if 0<= ni < m and 0 <= nj < n and color != visited[ni][nj] :
        roomCombinationList.add(roomCntBoard[(i,j)] + roomCntBoard[(ni,nj)])

print(roomCnt - 1)
print(max(roomMaxValue))
print(max(roomCombinationList))