import math

def prime(x) :
  for i in range(2, int(math.sqrt(x)) +1 ):
    if x % i == 0 :
      return False
  return True

count = 0
dp = []
for i in range(0,123456 * 2 + 1) :
  if prime(i) :
    count += 1
  dp.append(count)
    
answer = []

while 1 :
  n = int(input())
  if n== 0 :
    break
  answer.append(dp[2*n] - dp[n])
for a in answer :
  print(a)
  