import sys
arr = [ i for i in range(1,int(input())+1)]

while arr :
  if len(arr) == 1 :
    print(arr[0])
    break
  arr = [arr[i] for i in range(len(arr)) if i % 2 != 0]