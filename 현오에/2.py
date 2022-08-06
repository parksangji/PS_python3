import sys
input = sys.stdin.readline
n,x = map(int,input().split())
arr = list(map(int,input().split()))
value = sum(arr[:x])
ans1,ans2 = value,1
for i in range(x,n) :
  value += (arr[i] - arr[i-x])
  if ans1 < value : ans1 = value;ans2 = 1
  elif ans1 == value : ans2 += 1
if ans1 : print(ans1);print(ans2)
else : print("SAD")
