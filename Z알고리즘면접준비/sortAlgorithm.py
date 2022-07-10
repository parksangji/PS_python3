def mergeSort(arr) :
  def devide(low,high) :
    if high - low < 2 : return
    mid = (high + low)// 2
    devide(low,mid)
    devide(mid,high)
    conqure(low,mid,high)
  def conqure(low,mid, high) :
    tmp,l,h = [],low,mid
    while l < mid and h < high :
      if arr[l] < arr[h] : tmp.append(arr[l]) ; l += 1
      else : tmp.append(arr[h]) ; h += 1
    while l < mid : tmp.append(arr[l]) ; l += 1
    while h < high : tmp.append(arr[h]) ; h += 1
    for i in range(low,high) : arr[i] = tmp[i-low]
  return devide(0,len(arr))

def quickSort(arr) :
  def devide(low,high) :
    if low >= high : return
    mid = partition(low,high)
    devide(low,mid-1)
    devide(mid,high)

  def partition(low,high) :
    pivot = arr[(low+high)//2]
    while low <= high :
      while arr[low] < pivot :
        low +=1
      while arr[high] > pivot :
        high -= 1
      if low <= high :
        arr[low],arr[high] = arr[high], arr[low]
        high -=1
        low += 1
    return low
  return devide(0,len(arr)-1)

def insertSort(arr) :
  n = len(arr)
  print("insert sort : ",end = "")
  for i in range(1,n) :
    for j in range(i,0,-1) :
      if arr[j-1] > arr[j] :
        arr[j-1],arr[j] = arr[j],arr[j-1]

def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def bubbleSort(arr) :
  n = len(arr)
  print("bubble sort : ",end = "")
  for i in range(n-1,0,-1) :
    for j in range(i) :
      if arr[j] > arr[j+1] :
        arr[j],arr[j+1] = arr[j+1],arr[j]

arr = [1,-2,5,10,34]
quickSort(arr)
print(arr)