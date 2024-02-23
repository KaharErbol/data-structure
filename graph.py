graph = {}
vertices_no = 0

def add_vertex(v):
  global graph
  global vertices_no
  if v in graph:
    print(v, "is in graph.")
  else:
    vertices_no += 1
    graph[v] = []

def add_edge(v1, v2, e):
  global graph
  if v1 not in graph:
    print(v1, "does not exist.")
  elif v2 not in graph:
    print(v2, "does not exist.")
  else:
    temp = [v2, e]
    graph[v1].append(temp)

def print_graph():
  global graph
  for vertex in graph:
    for edges in graph[vertex]:
      print(vertex, " -> ", edges[0], " edge weight: ", edges[1])


add_vertex(1)
add_vertex(2)
add_vertex(3)
add_vertex(4)

add_edge(1, 2, 1)
add_edge(2, 3, 2)
add_edge(1, 4, 1)

print_graph()