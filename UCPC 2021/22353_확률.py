a,d,k = map(float,input().split())
d /= 100.0
k /= 100.0
answer = 0.0
idx = 1
prev = 1
while 1 :
  answer += idx * a * prev * d
  if d == 1 :
    break
  prev *= (1-d)
  d += d * k
  idx += 1
  if d >=1 :
    d = 1
print("{:.7f}".format(answer))