from bisect import bisect_left
n,*X = map(int,open(0).read().split())
arr = []
for x in X :
  if not arr : arr.append(x) ; continue
  if arr[-1] < x : arr.append(x)
  else : arr[bisect_left(arr,x) ] = x
print(len(arr))