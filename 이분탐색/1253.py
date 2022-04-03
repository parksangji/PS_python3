import sys

n = int(input())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
answer = 0
for i in range(n) :
  left = 0
  right = n-1
  target = arr[i]
  while left < right :
    sum = arr[left] + arr[right]
    if sum == target :
      if left != i and right != i :
        answer += 1
        break
      elif left == i :
        left += 1
      elif right == i :
        right -= 1
    elif target < sum :
      right -= 1
    else :
      left += 1
print(answer)