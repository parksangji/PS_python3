import sys; from collections import deque ;input = sys.stdin.readline
def init() :
  coin = []
  for i in range(n) :
    for j in range(m) :
      if arr[i][j] == 'o' :
        coin.append([i,j])
  return coin[0],coin[1]

def outRange(x,y) :
  if 0 <= x < n and 0 <= y < m :
    return False
  return True

def bfs(a,b,c,d) :
  q = deque()
  visited = {}
  q.append([a,b,c,d,0])
  visited[str(a) + str(b) + str(c) + str(d)] = True
  while q :
    a,b,c,d,cnt = q.popleft()
    if cnt >= 10 :
      continue
    for i in range(4) :
      aa,bb = a + dx[i],b + dy[i]
      cc,dd = c + dx[i],d + dy[i]
      if outRange(aa,bb) and outRange(cc,dd) :
        continue
      if outRange(aa,bb) or outRange(cc,dd) :
        return cnt+1
      if arr[aa][bb] == "#" :
        aa -= dx[i]
        bb -= dy[i]
      if arr[cc][dd] == "#" :
        cc -= dx[i]
        dd -= dy[i]
      flag = str(aa) + str(bb) + str(cc) + str(dd)
      if flag in visited :
        continue
      visited[flag] = True
      q.append([aa,bb,cc,dd,cnt+1])
  return -1
dx = [0,0,-1,1] ; dy = [-1,1,0,0]
n,m = map(int,input().split())
arr = [list(input().strip()) for _ in range(n)]
coin1,coin2 = init()
print(bfs(coin1[0],coin1[1],coin2[0],coin2[1]))