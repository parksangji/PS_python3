import sys ; input = sys.stdin.readline ; n = int(input())
dx = [0,0,-1,1] ; dy = [-1,1,0,0]

arr = [list(map(int,input().split())) for _ in range(n**2)]
matrix = [[0] * (n+1) for _ in range(n+1)] ;dict = {}

for cur,a,b,c,d  in arr :
  like = [a,b,c,d]
  dict[cur] = [a,b,c,d]
  mem = []
  for i in range(1,n+1) :
    for j in range(1,n+1) :
      if matrix[i][j] != 0 :
        continue
      empty = 0
      nearbylike = 0
      
      for k in range(4) :
        nx = i + dx[k]
        ny = j + dy[k]
        if 1<= nx < n+1 and 1<= ny < n+1 :
          if matrix[nx][ny] == 0 :
            empty += 1
          else :
            if matrix[nx][ny] in like :
              nearbylike += 1
      mem.append([nearbylike,empty,i,j])
  mem.sort(key = lambda x : [-x[0],-x[1],x[2],x[3]])
  matrix[mem[0][2]][mem[0][3]] = cur
answer = 0
for x in range(1,n+1) :
  for y in range(1,n+1) :
    cur = matrix[x][y]
    cnt = 0
    for i in range(4) :
      nx = x + dx[i]
      ny = y + dy[i]
      if 1<= nx < n+1 and 1 <= ny < n+1 and matrix[nx][ny] in dict[cur] :
        cnt +=1
    if cnt == 4 :
      answer += 1000
    elif cnt == 3 :
      answer += 100
    elif cnt == 2 :
      answer += 10
    else :
      answer += cnt
print(answer)
