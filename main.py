def next_permutation() :
  i = j = k = n
  while i >0 and arr[i-1] >= arr[i]: i -= 1
  if i == 0 : print(-1) ; return
  while arr[i-1] >= arr[j] : j-=1
  arr[i-1] , arr[j] = arr[j],arr[i-1]
  while i < k :
    arr[i],arr[k] = arr[k],arr[i]
    i += 1; k -= 1
  print(*arr)

n = int(input()) -1
arr = list(map(int,input().split()))
next_permutation()
