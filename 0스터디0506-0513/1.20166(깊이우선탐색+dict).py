import sys; n,m,k = map(int,sys.stdin.readline().split())

def dfs(x,y,depth,like) :
  if depth > max_ :
    return
  if like in dict :
    dict[like] += 1
  else :
    dict[like] = 1
  for i in range(8) :
    nx,ny = (x+dx[i]) % n, (y+dy[i])% m
    dfs(nx,ny,depth+1,like + alpha[nx][ny])

dx = [0,0,-1,1,1,1,-1,-1] ; dy = [1,-1,0,0,-1,1,-1,1]
alpha = [list(sys.stdin.readline().strip()) for _ in range(n)]
likestr = [sys.stdin.readline().strip() for _ in range(k)]
dict = {}

max_ = max([len(i) for i in likestr])

for i in range(n) :
  for j in range(m) :
    dfs(i,j,1,alpha[i][j])
for i in likestr :
  try :
    print(dict[i])
  except :
    print(0)