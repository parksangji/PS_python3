r,c = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(r)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs() :
  visited = [[False] * c for _ in range(r)]
  q = [[0,0]]
  visited[0][0] = True
  cnt = 0
  while q :
    x,y = q.pop(0) 
    for i in range(4) :
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
        if graph[nx][ny] == 1 :
          graph[nx][ny] = 0
          visited[nx][ny] = True
          cnt += 1
        else :
          q.append([nx,ny])
          visited[nx][ny] = True
  return cnt

time = 0
before = 0

while True :
  cnt = bfs()
  if cnt == 0 :
    print(time)
    print(before)
    break
  time += 1
  before =  cnt