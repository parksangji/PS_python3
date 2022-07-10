from collection import deque
indegree = [0]*(v+1)
graph[[] for _ in range(v+1)]

for _ in range(e):
  graph[a].append(b) #A에서 B로 이동 가능
  indegree[b] += 1
  
def topology_sort():
  result = []
  q = deque()
  
  for i in range(1,v+1):
    if indegree[i] == 0:
      q.append(i)
   
  while q:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
      indegree[i] -= 1
      if indegree[i] == 0:
        q.append(i)
      
  for i in result: print(i, end= ' ')
 
topology_sort()


"""
순서가 정해져 있는 일련의 작업을 차례대로 수행해야할 때 사용할 수 있는 알고리즘
방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것
선수과목을 고려한 학습 순서 설정을 생각해보면된다. 

진입 차수가 0인 노드를 큐에 넣는다.
진입차수 : 특정한 노드로 들어오는 간선의 개수
큐가 빌 때까지 다음의 과정을 반복한다.

큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거 한다.
새롭게 진입 차수가 0이 된 노드를 큐에 넣는다.


과정을 수행하는 동안 큐에서 빠져나간 노드를 순서대로 출력하면 위상 정렬을 수행한 결과가 된다.

위상 정렬의 특이 케이스 

사이클이 발생하는 경우  일반적인 위상 정렬의 경우 정확히 N개의 노드가 큐에서 출력이 된다. 노드가 N번 나오기 전에 큐가 비면 사이클이 발생한 것으로 이해할 수 있다. 
위상 정렬 결과가 1개가 아니라 여러 가지인 경우 특정 시점에 2개 이상의 노드가 큐에 한꺼번에 들어갈 때는 가능한 정렬 결과가 여러가지라는 의미가 된다.


차례대로 모든 노드를 확인하면서, 해당 노드에서 출발하는 간선을 차례대로 제거해야하므로 결과적으로 노드와 간선을 모두 확인해야한다는 측면에서 O(V+E)의 시간이 소요된다
"""
