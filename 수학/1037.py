n = int(input())

arr = list(map(int,input().split()))

arr.sort()

if len(arr) == 1 :
  print(arr[0] ** 2)
elif len(arr) == 2 :
  print(arr[0] * arr[1])
else :
  size = len(arr) // 2
  if len(arr) % 2 == 0 :
    print(arr[size] * arr[size-1])
  else :
    print(arr[size] ** 2)

