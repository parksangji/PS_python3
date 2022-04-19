import sys; n = int(sys.stdin.readline());v = [list(map(int,sys.stdin.readline().split())) for _ in range(n)];v += [v[0]];a = 0 ; b = 0
for i in range(1,len(v)) :
  a += (v[i-1][0] * v[i][1])
  b += (v[i-1][1] * v[i][0])
print(abs(a-b) / 2)