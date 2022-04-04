n = int(input())
arr = [str(input())for _ in range(n)]
# print(arr)

def divideConqure(size,x,y) :
  for i in range(x,x+size) :
    for j in range(y,y+size) :
      if arr[x][y] is not arr[i][j] :
        print("(" , end = '')
        divideConqure(size//2,x,y)
        divideConqure(size//2,x,y+size//2)
        divideConqure(size//2,x+size//2,y)
        divideConqure(size//2,x+size//2,y+size//2)
        print(")" , end = '')
        return
  print(arr[x][y] , end = '')
divideConqure(n,0,0)