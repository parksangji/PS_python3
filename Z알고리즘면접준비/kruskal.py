def find_parent(parent,x):
  if parent[x] != x:
    parent[x] = find_parent(parent,parent[x])
  return parent[x]
def union_parent(parent,a,b):
  a = find_parent(parent,a)
  b = find_parent(parent,b)
  if a<b: parent[b] = a
  else: parent[a] = b
      
parnet= [0] * (v+1)

edges = []
result = []
for i in range(1,v+1):
  parent[i] = i
 
for i in range(e):
  a,b,c = map(int,input().split())
  edges.append((cost,a,b)) 
 
edges.sort()
for edge in edges:
  const, a, b = edge
  if find_parent(parent,a) != find_parent(parent,b): 
    union_parent(parent,a,b)
    result += cost
print(resut)

"""
그래프의 모든 간선을 가중치의 오름차순으로 정렬한 뒤 신장 트리에 하나씩 추가해 간다.
간선을 트리에 추가했을 때 이미 추가한 간선들과 합쳐 사이클을 이루는지 여부를 판단한다.

두 정점이 주어졌을 때 이들이 같은 컴포넌트에 속하는지 확인하고, 아닐 경우 두 컴포넌트를 합친다. 

서로소 집합 자료구조의 find, union 연산을 사용한다.
서로소 집합을 쓰지 않고 DFS 할 경우 DFS의 시간 복잡도인 O(|V|+|E|) 에 E를 곱해 O(E^2)이 된다


최소 신장 트리에 포함되어 있는 간선의 비용만 모두 더 하면 그 값이 최종 비용이 된다.

시간 복잡도 
간선의 개수가 E개일 때, O(ElogE)이다. 가장 오래 시간이 걸리는 부분이 정렬이고 정렬은 E개의 데이터를 정렬할 때 O(ElogE)이기 때문이다.
"""