import sys

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(5)]

answer = set()

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def dfs(x,y,depth,string) :
  if depth == 5:
    answer.add(string)
    return

  for i in range(4) :
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < 5 and 0 <= ny < 5 :
      dfs(nx,ny,depth+1,string + str(arr[nx][ny]))


for i in range(5) :
  for j in range(5) :
    dfs(i,j,0,str(arr[i][j]))
print(len(answer))