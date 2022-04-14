from bisect import *
n = int(input())
crain = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

crain.sort(reverse = True)
box.sort()

if crain[0] < box[-1]:
	print(-1)
else:
	cnt = 0
	while box:
	    cnt += 1
	    for c in crain:
	        right = bisect_right(box, c)
	        if box and box[right-1] <= c:
		        box.pop(right-1)
	print(cnt)