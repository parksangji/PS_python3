import sys
# 1051 다이나믹 프로그래밍 + 브루트포스
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(map(int,input().strip())) for _ in range(n)]
answer = 0
for i in range(n) :
  for j in range(m) :
    for k in range(min(n,m)) :
      if i + k < n and j + k < m and arr[i][j] == arr[i][j+k] == arr[i+k][j] == arr[i+k][j+k] :
        answer = max(answer, (k+1) ** 2)

print(answer)