import sys,heapq; input = sys.stdin.readline;maxq = [];minq = []
answer = []
for _ in range(int(input())) :
  a = int(input())
  if len(maxq) == len(minq) :
    heapq.heappush(maxq,-a)
  else :
    heapq.heappush(minq,a)

  if maxq and minq and -maxq[0] > minq[0] :
    maxtop = -heapq.heappop(maxq)
    mintop = heapq.heappop(minq)
    heapq.heappush(maxq,-mintop)
    heapq.heappush(minq,maxtop) 

  answer.append(str(-maxq[0]))

print('\n'.join(answer))