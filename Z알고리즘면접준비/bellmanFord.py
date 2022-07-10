def BellmanFord(src,graph) :
  inf = 987654321
  dist = [inf for i in range(len(graph) + 1)]
  dist[src] =0
  for i in range(len(graph)) :
    for u,v,w in graph :
      if dist[u] != inf and dist[u] + w < dist[v] :
        dist[v] = dist[u] + w

  for u,v,w in graph :
    if dist[u] != inf and dist[u] + w < dist[v] :
      print("cycle")
      return -1
  else : return dist
