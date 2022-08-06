def Kadane(arr,n) :
  dp = [0 for _ in range(n)]
  dp[0] = arr[0]
  for i in range(1,n) :
    dp[i] = max(arr[i],dp[i-1] + arr[i])
  return max(dp)

arr = [-5, 2, 3, 4, -7, -6, 6]
n = len(arr)
 
negative = Kadane([-arr[i] for i in range(n)],n)
possive = Kadane(arr,n)

print(max(possive, sum(arr) + negative))