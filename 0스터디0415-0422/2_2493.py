import sys; input = sys.stdin.readline
n = int(input()) ; arr = list(map(int,input().split())) ; q = [[n-1,arr[-1]]] ; answer = [0] * (n)

for i in range(n-2,-1,-1) :
  if  q[-1][1] < arr[i]: 
    while q and q[-1][1] < arr[i] :
      answer[q.pop()[0]] = i+1
    q.append([i,arr[i]])
  else :
    q.append([i,arr[i]])

for a in answer :
  print(a,end = " ")