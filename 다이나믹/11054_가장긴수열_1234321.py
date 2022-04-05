n = int(input())

arr = list(map(int,input().split()))

dp1 = [0] * n
dp2 = [0] * n
answer = 0

for i in range(n) :

  dp1[i] = 1
  for j in range(i) :
    if arr[j] < arr[i] and dp1[i] < dp1[j] + 1:
      dp1[i] = dp1[j] + 1
for i in range(n-1,-1,-1) :
  dp2[i] = 1
  for j in range(n-1,i,-1) :
    if arr[j] < arr[i] and dp2[i] < dp2[j] + 1 :
      dp2[i] = dp2[j] + 1

  answer = max(dp2[i] + dp1[i] - 1,answer)

print(answer)
"""
10
1 5 2 1 4 3 4 5 2 1

"""