import sys

def bfs() :
  q = [[x,y]]

  while q :
    qx,qy = q.pop(0)

    if abs(xx- qx) + abs(yy - qy) <= 1000 :
      return "happy"
    
    for i in range(n) :
      if not visited[i] :
        nx,ny = gs25[i]
        if abs(nx - qx) + abs(ny - qy) <= 1000 :
          q.append([nx,ny])
          visited[i] = True
  return "sad"
        
for i in range(int(sys.stdin.readline())) :
  n = int(sys.stdin.readline())
  visited = [False] * n
  gs25 = []
  x,y = map(int,sys.stdin.readline().split())
  for _ in range(n) :
    gs25.append(list(map(int,sys.stdin.readline().split())))
  xx,yy = map(int,sys.stdin.readline().split()) 
  print(bfs())
