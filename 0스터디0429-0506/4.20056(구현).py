import sys; input = sys.stdin.readline; n,m,k = map(int,input().split())

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

board = [[[] for _ in range(n)] for _ in range(n)]
fireball = []
answer = 0 

for _ in range(m) :
  fireball.append(list(map(int,input().split())))

for _ in range(k) :

  while fireball :
    r,c,m,s,d = fireball.pop() 
    board[(r + dx[d] * s) % n][(c + dy[d] * s) % n].append([m,s,d])

  for i in range(n) :
    for j in range(n) :
      if len(board[i][j]) == 1 :
        fireball.append([i,j] + board[i][j].pop())
      if len(board[i][j]) >= 2 :
        sumM,sumS,cnt_odd,cnt_even,cnt = 0,0,0,0,len(board[i][j])
        while board[i][j] :
          m,s,d = board[i][j].pop()
          sumM += m 
          sumS += s
          if d % 2 :
            cnt_even += 1
          else :
            cnt_odd += 1
        m = sumM // 5 ; s = sumS // cnt ; d = [0,2,4,6] if cnt_even == cnt or cnt_odd == cnt else [1,3,5,7]
        if m == 0 :
          continue
        for dir in d :
          fireball.append([i,j,m,s,dir])

for r,c,m,s,d in fireball :
  answer += m 
print(answer)