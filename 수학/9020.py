t = int(input())
import math
prime = []
flag = True
for i in range(10001) :
  for j in range(2, int(math.sqrt(i)) +1 ) :
    if i % j == 0 :
      flag = False
      break
  prime.append(flag)
  flag = True

for i in range(t) :
  n = int(input()) 
  tmp1 = n//2
  if prime[tmp1] :
    print(tmp1,tmp1)
  else :
    tmp1 = n//2 
    while tmp1 != n :
      tmp1 += 1
      tmp2 = n - tmp1
      if prime[tmp1] and prime[tmp2] :
        print(tmp2,tmp1)
        break
