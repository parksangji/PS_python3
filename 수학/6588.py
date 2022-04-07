import sys
import math
def prime(n) :

  for i in range(2,int(math.sqrt(n) + 1)) :
    if n % i == 0 :
      return False
  return True

def solution(n) :

  start = 2
  end = n-1 
  while start<= end :
    if  not prime(start) :
      start += 1
      continue
    if not prime(end) :
      end -= 1
      continue
    if start + end  == n :
      return start,end
    elif n < start + end :
      end -=1
    else :
      start += 1
      
  

while True :
  n = int(sys.stdin.readline())
  if n == 0 :
    break
  a,b = solution(n) 
  print("{0} = {1} + {2}".format(n,a,b))
  