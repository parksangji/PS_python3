import sys; n,m = map(int,sys.stdin.readline().split()) ; dx,dy = [0,0,-1,1],[1,-1,0,0]
arr = [list(sys.stdin.readline().strip()) for _ in range(n)]

def possible() :
  ret,k = 0,3
  for i in range(n) :
    for j in range(m) :
      k = 4
      while k :
        k -= 1
        nx,ny = i + dx[k],j + dy[k]
        if nx < 0 or nx >= n or ny < 0 or ny >=m :
          continue
        if arr[nx][ny] != arr[i][j] :
          break
      if k == 0 :
        ret += 1
  def divide_conqure(n) :
    if n== 0 :
      return 1
    if n== 1 :
      return 2
    if n % 2 :
      return (divide_conqure(n-1) * 2) % 1000000007
    else :
      n = divide_conqure(n//2)
      return (n * n) % 1000000007
  return divide_conqure(ret)
print(possible())