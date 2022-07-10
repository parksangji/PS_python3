import sys,collections
input = sys.stdin.readline

N,M,R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
dr,dc = [1,0,-1,0],[0,1,0,-1]

def rotation() :
  for depth in range(min(N,M)//2) :
    r = c = depth
    q = collections.deque([])
    for i in range(4) :
      while True :
        nr,nc = r + dr[i],c + dc[i]
        if depth<= nr < N-depth and depth<= nc < M-depth :
          q.append(arr[r][c])
          r,c = nr,nc
        else :
          break
    for _ in range(R % ((N - depth * 2) * 2 + (M - depth * 2) * 2 - 4)) :
      q.appendleft(q.pop())
    for i in range(4) :
      while True :
        nr,nc = r + dr[i],c + dc[i]
        if depth <= nr < N - depth and depth <= nc < M -depth:
          arr[r][c] = q.popleft()
          r,c, = nr,nc
        else :
          break
    
rotation()

for i in range(N):
  print(*arr[i])