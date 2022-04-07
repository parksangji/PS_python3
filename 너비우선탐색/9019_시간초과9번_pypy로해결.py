from collections import deque
import sys
def d(n) :
  n *= 2
  if n > 9999 :
    return n % 10000
  return n
def s(n) :
  if n == 0 :
    return 9999
  else :
    return n-1
def l(n) :
  a = n % 1000
  b = n // 1000

  return a * 10 + b
def r(n) :
  a  = n % 10
  b  = n // 10

  return a * 1000 + b

def bfs(a,b) :
  p = deque()
  p.append([a,""])
  visited = set()
  visited.add(a)
  while p :
    cur,op = p.popleft()

    if cur == b :
      return op
    tmp = d(cur)
    if tmp not in visited :
      visited.add(tmp)
      p.append([tmp,op + "D"])
    tmp = s(cur)
    if tmp not in visited :
      visited.add(tmp)
      p.append([tmp,op + "S"])
    tmp = l(cur)
    if tmp not in visited :
      visited.add(tmp)
      p.append([tmp,op + "L"])
    tmp = r(cur)
    if tmp not in visited :
      visited.add(tmp)
      p.append([tmp,op + "R"])
    
for i in range(int(input())) :
  a,b = map(int,sys.stdin.readline().split())
  print(bfs(a,b))
