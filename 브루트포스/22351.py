import sys
def select(start,size) :
  cur = ''
  end = str(start)
  for i in range(start,1000) :
    if len(cur) >= size :
      break
    cur += str(i)
    end = str(i)
  return [cur,start,end]
def solve() :
  case = []
  case.append(select(int(a[0]),len(a)))
  if len(a) >= 2 :
    case.append(select(int(a[:2]),len(a)))
  if len(a) >= 3 :
    case.append(select(int(a[:3]),len(a)))
  
  for cur,start,end in case :
    if cur == a :
      print(start,end)
      break
a = input()
solve()