import sys,collections
input = sys.stdin.readline
k = int(input())
wheel = [collections.deque(list(map(int,input().strip()))) for _ in range(k)]

def rotation(start,dir) :
  cur,d = start,dir
  rotationWheel = [(cur,dir)]
  while cur < k-1 and wheel[cur][2] != wheel[cur+1][-2]:
    rotationWheel.append((cur+1,-d))
    cur += 1; d = -d
  cur,d = start,dir
  while cur > 0 and wheel[cur][-2] != wheel[cur-1][2] :
    rotationWheel.append((cur-1,-d))
    cur -=1 ; d = -d

  for cur,dir in set(rotationWheel) :
    wheel[cur].rotate(dir)

for _ in range(int(input())) :
  start,dir = map(int,input().split())
  rotation(start-1,dir)

print(sum(1 for i in range(k) if wheel[i][0]))