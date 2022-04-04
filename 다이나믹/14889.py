import sys
from itertools import combinations
n = int(input())

matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
member = [i for i in range(n)]
team = [teams for teams in list(combinations(member,n//2))]

answer = 10000

for i in range(len(team)//2) :

  a = 0
  b = 0
  
  for j in range(n//2) :
    for k in team[i] :
      a += matrix[team[i][j]][k]
  for j in range(n//2) :
    for k in team[-i-1] :
      b += matrix[team[-i-1][j]][k] 
  answer = min(answer,abs(a-b))
print(answer)