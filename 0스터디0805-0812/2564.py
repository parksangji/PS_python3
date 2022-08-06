import sys; input = sys.stdin.readline
w,h = map(int,input().split())
dist= []
for _ in range(int(input()) + 1) :
  a,b = map(int,input().split())
  if a in [1,2] : dist.append(b if a == 1 else 2*w + h -b)
  else : dist.append(w + b if a == 4 else 2 * w + 2 * h - b)
print(sum( min(abs(dist[-1] - v), 2 * (w+h) - abs(dist[-1] - v)) for v in dist[:-1]))