import sys
input = sys.stdin.readline

n,jimin,hansu = map(int,input().split())
cnt = 0
print(-jimin^-hansu)
while jimin != hansu :
  jimin -= jimin//2
  hansu -= hansu//2
  cnt += 1
else :
  print(cnt)