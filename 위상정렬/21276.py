import sys; from collections import deque 

n = int(sys.stdin.readline())
relation = {}
tmp = {}
name = []
for i in sys.stdin.readline().strip().split(' ') :
  relation[i] = []
  tmp[i] = 0

for _ in range(int(sys.stdin.readline())) :
  child,parent = sys.stdin.readline().strip().split(' ')
  tmp[child] += 1
  relation[parent].append(child)
name = sorted(list(tmp))
q = []
for i in tmp :
  if tmp[i] == 0 :
    q.append(i)
q = deque(sorted(q))
print(len(q))
for i in q :
  print(i,end = " ")
print()
answer = {}
while q :
  cur = q.popleft()
  answer[cur] = []
  for child in relation[cur] :
    tmp[child] -= 1
    if tmp[child] == 0 :
      answer[cur].append(child)
      q.append(child)

for n in name :
  print(n,len(answer[n])," ".join(sorted(answer[n])))