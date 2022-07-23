n,*x= map(int,open(0).read().split()); x.sort()
minV,s,e,ans = 2e+10,0,n-1,None
while s < e :
  m = x[s] + x[e]
  if abs(m) < minV :
    minV,ans = abs(m),(x[s],x[e])
  if minV == 0 : break
  elif m < 0 : s += 1
  else : e -= 1
print(*ans)