import sys,collections ; input = sys.stdin.readline
m,n,p = map(int,input().split())
board = [list(input().strip()) for _ in range(m)]
playerPower = { x : int(y) for x,y in [input().strip().split() for _ in range(p)]}
bosshp = int(input()) ; bossPos = 0
visited = [[False] * n for _ in range(m)]
dx = [0,0,-1,1] ; dy = [-1,1,0,0] 


## boss 위치 찾기
for i in range(m) :
  flag = False  
  for j in range(n) :
    if board[i][j] == "B" :
      bossPos = (i,j)
      flag = True
      break
  if flag :
    break
q = collections.deque([bossPos])
visited[bossPos[0]][bossPos[1]] = True
attack = []

while bosshp > 0 :
  size = len(q)
  while size :
    x,y = q.popleft()
    size -= 1
    for i in range(4) :
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx < m and 0 <= ny < n and board[nx][ny] != "X" and not visited[nx][ny] :
        if board[nx][ny] == '.' :
          q.append([nx,ny])
          visited[nx][ny] = True
        else :
          q.append([nx,ny])
          visited[nx][ny] = True
          attack.append(board[nx][ny])
  for a in attack :
    bosshp -= playerPower[a]
print(len(attack))