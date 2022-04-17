import sys,heapq;n,k= map(int,sys.stdin.readline().split())

running = []; os = [(0,i) for i in range(k)]; terminated = [] ;heapq.heapify(os); last = 0
for _ in range(n) :
  id_,time_ = map(int,sys.stdin.readline().split())

  waiting,num_ = heapq.heappop(os)
  waiting += time_
  heapq.heappush(os,(waiting,num_))

  if len(running) >= k :
    time,num,id = heapq.heappop(running)
    terminated.append(id)
    last = time
  heapq.heappush(running,(time_+last,-num_,id_))

while running :
  time,num,id = heapq.heappop(running)
  terminated.append(id)

print(sum([ i * terminated[i-1] for i in range(1,n+1)]))