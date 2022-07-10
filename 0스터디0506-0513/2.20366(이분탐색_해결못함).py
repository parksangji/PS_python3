import sys;minDist = sys.maxsize
n = int(sys.stdin.readline()) 
h = sorted(list(map(int,sys.stdin.readline().split())))

for i in range(n) :
  for j in range(i+3,n) :
    left,right = i+1,j-1 
    while left < right :
      dist = (h[i] + h[j]) - (h[left] + h[right])
      if abs(dist) < minDist :
        minDist = abs(dist)
      if dist < 0 :
        right -=1 
      else :
        left += 1
print(minDist)

"""
import sys,itertools;
n = int(sys.stdin.readline())
h = list(map(int,sys.stdin.readline().split()))
hh = sorted([(hi + hj,{i,j}) for i,hi in enumerate(h) for j,hj in enumerate(h[:i])])
print(min(abs(hh[i][0] - hh[i+1][0]) for i in range(len(hh) - 1) if not (hh[i][1] & hh[i+1][1])))
"""