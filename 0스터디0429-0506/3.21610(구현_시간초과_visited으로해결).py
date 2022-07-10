import sys; input = sys.stdin.readline
n,m = map(int,input().split())

a = [list(map(int,input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]
slicedx = [-1,-1,1,1]
slicedy = [-1,1,1,-1]
cloud = [[n-1,0],[n-1,1],[n-2,0],[n-2,1]]

def cloudfunction(dir,move,cnt) :
  uncloud = []
  while cloud :
    x,y = cloud.pop()
    x = (x + dx[dir] * move) % n
    y = (y + dy[dir] * move) % n
    a[x][y] += 1
    uncloud.append([x,y])
    visited[x][y] = cnt
  for x,y in uncloud :
    for i in range(4) :
      nx = x + slicedx[i]
      ny = y + slicedy[i]
      if 0<= nx < n and 0<= ny < n and a[nx][ny] >= 1 :
        a[x][y] += 1
  for i in range(n) :
      for j in range(n) :
        if a[i][j] >= 2 and visited[i][j] != cnt :
          a[i][j] -= 2
          cloud.append([i,j])
for i in range(m) :
  d,s = map(int,input().split())
  cloudfunction(d-1,s,i+1)
print(sum([sum(i) for i in a]))