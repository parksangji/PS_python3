import heapq
def prim(src,edges):
  mst = []
  graph = [[] for _ in range(v)]
  
  for weight,n1,n2 in edges:
    graph[n1].append((weight,n1,n2))
    graph[n2].append((weight,n2,n1))
    
  
  connected_nodes = set(src)
  candidate_edge_list = graph[src]
  heaplify(candidate_edge_list)
  
  while candidate_edge_list :
    weight,n1,n2 = heapq.heappop(candidate_edge_list)
    if n2 not in connected_nodes :
      connected_nodes.append(n2)
      mst.append((weight,n1,n2))
      
      for edge in graph[n2]:
        if edge[2] not in connected_nodes:
          heapq.heappush(candidate_edge_list,edge)
    
  return mst

"""
하나의 시작점으로 구성된 트리에 간선을 하나씩 추가하며 스패닝 트리가 될 때까지 키워 간다.
이미 만들어진 트리에 인접한 간선만을 고려한다는 점을 제외하면 프림 알고리즘은 크루스칼 알고리즘과 완전히 똑같다.

각 정점이 트리에 포함되었는지 여부를 나타내는 배열을 둔다
각 차례마다 트리에 속하지 않은 정점에 대해 트리와 이 정점을 연결하는 가장 짧은 간선 정보를 저장한다. 
각 정점을 순회하면서 다음에 추가할 정점을 찾는다.
"""