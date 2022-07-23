n,*x = map(int,open(0).read().split());x.sort()
max_value,left,right,answer = max(x),0,n-1,(0,0)
while left< right :
  value = x[left] + x[right]
  if abs(value) < max_value :
    answer = (x[left],x[right])
    max_value = abs(value)
    if max_value == 0 :
      break
  if value < 0 : left +=1
  else : right -=1
print(*answer)