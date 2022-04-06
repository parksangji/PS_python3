import sys

graph = [list(map(int,sys.stdin.readline().split())) for _ in range(9)]

q = []
cnt = 0

def check(x,y,a) :

  for i in range(9) :
    if graph[i][y] == a and i != x :
      return False
    if graph[x][i] == a and i != y :
      return False
  xx, yy = 3 * (x//3),3 * (y//3)
  for i in range(xx,xx + 3) :
    for j in range(yy,yy+ 3) :
      if graph[i][j] == a and i != x and j != y :
        return False

  return True
  
def dfs(n) :
  if n == cnt :
    for i in range(9) :
        print(*graph[i])
    exit(0)
  x,y = q[n]
  for i in range(1,10) :
    if check(x,y,i) :
      graph[x][y] = i
      dfs(n+1)
      graph[x][y] = 0


for i in range(9) :
  for j in range(9) :
    if graph[i][j] == 0 :
      q.append([i,j]) 
      cnt += 1

dfs(0)