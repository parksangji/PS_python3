import sys;
def zeroone(n) :
  if n== 0 :
    return 0 
  if n == 1 :
    return 1
  if n%2 :
    return 1 - zeroone(n//2)
  else :
    return zeroone(n//2)
print(zeroone(int(sys.stdin.readline())-1))
