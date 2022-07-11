import sys
input = sys.stdin.readline

R,C = map(int,input().split())
board = [list(input().strip()) for _ in range(R)]
dx,dy = [-1,0,1,0] , [0,1,0,-1]
dir = [["|","+","1","4"], ["-","+","3","4"],["|","+","2","3"],["-","+","1","2"]]

def change(x,y) :
  global flag
  tmp = []
  for i in range(4) :
    nx,ny = x + dx[i],y + dy[i]
    if 0<= nx < R and 0 <= ny < C and board[nx][ny] != '.' and board[nx][ny] in dir[i]:
      tmp.append(i)
  print(x+1,y+1,end = " ")
  if len(tmp) == 4 :
    print("+")
  else :
    if [1,3]  == tmp : print("-")
    elif [0,2] == tmp : print("|")
    elif [1,2] == tmp : print("1")
    elif [0,1] == tmp : print("2")
    elif [0,3] == tmp : print("3")
    else : print("4")
  flag = True
flag = False

for i in range(R) :
  if flag : break
  for j in range(C) :
    if flag : break
    if board[i][j] == "|" :
      if board[i-1][j] == '.' : change(i-1,j) 
      elif board[i+1][j] == '.' : change(i+1,j)
    elif board[i][j] == '-' :
      if board[i][j-1] == '.' : change(i,j-1)
      elif board[i][j+1] == '.' : change(i,j+1)
    elif board[i][j] == '1' :
      if board[i][j+1] == '.' : change(i,j+1)
      elif board[i+1][j] == '.' : change(i+1,j)
    elif board[i][j] == '2' :
      if board[i-1][j] == '.' : change(i-1,j) 
      elif board[i][j+1] == '.' : change(i,j+1)
    elif board[i][j] == '3' :
      if board[i-1][j] == '.' : change(i-1,j)
      elif board[i][j-1] == '4' : change(i,j-1)
    elif board[i][j] == '4' :
      if board[i][j-1] == '.' : change(i,j-1)
      elif board[i+1][j] == '.' : change(i+1,j)
    elif board[i][j] == '+' :
      for k in range(4) :
        nx,ny = i + dx[k], j + dy[k]
        if board[nx][ny] == '.' :
          change(nx,ny)
          break

