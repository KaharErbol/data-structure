def bfs(graph, root):
  visited = set()
  result = []
  q = []
  q.append(root)

  while q:
    node = q.pop(0)
    if not node in visited:
      visited.add(node)
      result.append(node)
      for neighbor in graph[node]:
        q.append(neighbor)
      

  return result




graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

order = bfs(graph, 'A')

print(order)






