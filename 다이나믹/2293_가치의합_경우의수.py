n,k = map(int,input().split())
arr = [int(input()) for _ in range(n)]

dp = [0] * (k+1)
dp[0] = 1
for i in range(n) :
  for j in range(arr[i],k+1) :
    dp[j] = dp[j] + dp[j- arr[i]]
    
print(dp[k])

"""
n,m=map(int,input().split());l=[1]+[0]*m
for i in range(n):
 c=int(input())
 for i in range(m-c+1):l[i+c]+=l[i]
print(l[-1])

"""