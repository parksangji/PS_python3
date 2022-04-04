"""
e,s,m = map(int,input().split())
ee = 1
ss = 1
mm = 1
cnt = 1

while True :
  if e == ee and s == ss and m == mm :
    print(cnt)
    break
  cnt += 1
  ee += 1
  mm += 1
  ss += 1
  if ee == 16 :
    ee = 1
  if ss == 29 :
    ss = 1
  if mm == 20 :
    mm = 1
"""

e,s,m = map(int,input().split()); ans = s

while ans % 15 is not e % 15 or ans % 19 is not m % 19 :
  ans += 28

print(ans)
  
