n = int(input())

arr = [list(map(int,input().split())) for _ in range()]


def devide(x,y,size) :
  ret = [0,0,0]
  tmp = []
  for i in range(3) :
    for j in range(3) :
      tmp = cnt(x + i * size//3,y + j * size//3,size//3)
      ret[0] += tmp[0];ret[1] += tmp[1];ret[2] += tmp[2]
  return ret

def cnt(x,y,size) :
  for i in range(size) :
    for j in range(size) :
      if arr[x][y] != arr[x+i][y+j] :
        return devide(x,y,size)
  ret = [0,0,0]
  ret[arr[x][y] + 1] += 1
  return ret

ret = cnt(0,0,n)

for i in ret :
  print(i)