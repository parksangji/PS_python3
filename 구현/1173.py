# 브론즈 2 운동
import sys
N, m, M, T, R = map(int,sys.stdin.readline().split())

n = 0; cnt = 0 ;x = m;
while True :
  if cnt > 100000 :
    print(-1)
    break
  if n >= N :
    print(cnt)
    break
  if x + T <= M :
    x += T
    n += 1
  else :
    if m <= x - R :
      x -= R
    else :
      x = m
  cnt += 1