n = int(input())
arr = list(map(int,input().split()))
m = int(input())

tree = {}
for i in range(n) :
  if i == m or arr[i] == m :
    continue
  if arr[i] in tree :
    tree[arr[i]].append(i)
  else :
    tree[arr[i]] = [i]

answer = 0
q = []
if -1 in tree :
  q = [-1]
else :
  q = []
while q :
  node = q.pop()
  if node not in tree :
    answer += 1
  else :
    q += tree[node]
print(answer)