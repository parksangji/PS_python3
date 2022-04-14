import sys

a,b = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
arr.extend(list(map(int,sys.stdin.readline().split())))
for i in sorted(arr) :
  print(i,end = " ")