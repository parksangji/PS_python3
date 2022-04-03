import sys
from collections import Counter
n = int(sys.stdin.readline())
arr = []
for _ in range(n) :
  arr.append(int(sys.stdin.readline()))
arr.sort()
nums = Counter(arr).most_common()
print(round(sum(arr)/n))
print(arr[n//2])
if len(nums) > 1 : 
  if nums[0][1] == nums[1][1] : 
    print(nums[1][0]) 
  else : 
    print(nums[0][0]) 
else : 
  print(nums[0][0])
print(arr[-1] - arr[0])