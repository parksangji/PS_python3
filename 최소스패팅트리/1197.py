import sys; input = sys.stdin.readline

v,e = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(e)]
arr.sort(key = lambda x : x[2])
root = [i for i in range(v+1)]
def findroot(cur) :
  if root[cur] == cur :
      return cur
  root[cur] = findroot(root[cur])
  return root[cur]

def union(a,b) :
  a = findroot(a) 
  b = findroot(b)
  if a == b :
    return False
  if a > b :
    root[b] = a
  else :
    root[a] = b
  return True

answer = 0
while arr :
  a,b,c = arr.pop(0)
  if(union(a,b)) :
    answer += c
  
print(answer)