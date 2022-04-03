import sys

s = str(input())
m = int(input())

cursor = len(s)

for i in range(m) :
  op = list(map,sys.stdin.readline().split())
  if op[0] == 'P' :
    
    