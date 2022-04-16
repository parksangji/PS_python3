import sys; input = sys.stdin.readline 
n = int(input())
arr = list(map(int,input().split()))
answer = [-1] * n
stack = [[arr[0],0]]
for i in range(1,n) :
  if stack[-1][0] < arr[i] :
    while stack and stack[-1][0] < arr[i] :
      answer[stack.pop()[1]] = arr[i]
    stack.append([arr[i],i])
  else :
    stack.append([arr[i],i])

for a in answer :
  print(a,end = " ")