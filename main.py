import sys; board = [list(map(int,sys.stdin.readline().strip())) for _ in range(9)]

def check(x,y,i) :
  for xx in range(9) :
    if xx != x and board[xx][y] == i :
      return False
  for yy in range(9) :
    if yy != y and board[x][yy] == i :
      return False
  xx,yy =( x //3) * 3 ,(y//3) * 3 
  for a in range(xx,xx+3) :
    for b in range(yy,yy+3) :
      if a != x and b != y and board[a][b] == i :
        return False
  return True

def dfs(cnt) :
  if cnt == n :
    for i in range(9) :
      for j in range(9) :
        print(board[i][j],end="")
      print()
    exit(0)
  x,y = q[cnt] 
  for i in range(1,10) :
    if check(x,y,i) :
      board[x][y] = i
      dfs(cnt+1)
      board[x][y] = 0

q = []
for i in range(9) :
  for j in range(9) :
    if board[i][j] == 0 :
      q.append([i,j])
n = len(q)
dfs(0)
