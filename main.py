import sys; n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
start = 0; end = n-1
compare = int(sys.maxsize)
answer = []
while start < end :
  sum = arr[start] + arr[end]
  if abs(sum) < abs(compare) :
    compare = sum
    answer = [arr[start],arr[end]]
  if 0 <= sum :
    end -= 1
  else :
    start += 1
print(answer[0],answer[1])