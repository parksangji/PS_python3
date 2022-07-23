n = int(input())
arr = list(map(int,input().split()))
list = [0]

for i in range(n) :
  a = arr[i]
  if list[-1] < a :
    list.append(a) 
  else :
    start =0
    end = len(list)
    while start < end :
      mid = (start+end)//2
      if list[mid] < a :
        start = mid +1 
      else :
        end = mid
    list[end] = a
print(len(list) - 1)