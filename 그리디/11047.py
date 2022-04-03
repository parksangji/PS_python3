n,k = map(int,input().split())

arr = []
answer = 0

for i in range(n) :
  arr.append(int(input()))
arr.sort(reverse =True)

for i in range(n) :
  if k <= 0 :
    break
  if arr[i] <= k :
    answer += (k // arr[i])
    k  %= arr[i]
  else : 
    continue
    
print(answer)