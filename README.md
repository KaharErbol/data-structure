# data-structure
<a id="top"></a>

## Content
1. [Definition of Graph Theory](#graph)
2. [Types of Graphs](#types-of-graphs)
3. [Special Graphs](#special-graphs)
4. [Representing Graphs](#representing-graphs)
5. [Common Graph Theory Problems](#common-graph-theory-problems)
6. [Depth First Search](#depth-first-search)

## Graph
Graph theory is the mathematical theory of the properties and applications
of graphs (networks).

### Types of Graphs
<a id="top" href="#top">[Back to Top](#top)</a>

1. Undirected Graph
...edges have no orientation.

2. Directed Graph
...edges have orientation.

3. Weighted Graphs
...edges can have certain weights to represent an arbitrary value such as cost, distance, quantity, etc...

### Special Graphs
<a id="top" href="#top">[Back to Top](#top)</a>

Below are only a few special graphs, there are more than these.
1. Trees
...undirected graph with no cycles. It is a connected graph with N nodes and N-1 edges.
![trees graph](./imgs/graph_tress.png)

2. Rooted Trees
It is a tree with a designated root node where every edges points away from or
towards the root node. Points away called arborescence (out-tree), otherwise it is called anti-arborescence (in-tree).
![rooted trees](./imgs/rooted_trees.png)

3. Directed Acyclic Graphs (DAGs)
- directed graphs with no cycles.
- important in representing structures with dependencies(Scheduler, Bill System...).
- several efficient algorithms exist to operate on DAGs.
- all out-trees are DAGs, but not all DAGs are out-tree.
![DAGs](./imgs/DAGs.png)

4. Bipartite Graph
- vertices can be split into two groups U, V such that every edge connects between U and V.
- the graph is a two colorable or there is no odd length cycle.
![bipartite graph](./imgs/bipartite_graph.png)

5. Complete Graphs
- there is a unique edge between every pair of nodes.
- a complete graph with n vertices is denoted as the graph K<sub>n</sub>.
- often seen as worse case possible graph.
![complete graph](./imgs/complete_graph.png)

### Representing Graphs
<a id="top" href="#top">[Back to Top](#top)</a>

#### Adjacency Matrix   
Adjacency matrix m is used to represent graphs.
- the cell m[i][j] represents the edge weight of going from node i to node j.
- it is often assumed that the edge of going from a node to itself has a cost of zero.

*Pros*
- Space efficient for representing dense graphs. 
- Edge weight lookup is O(1).
- Simplest graph representation.

*Cons*
- Requires O(V^2)
- Iterating over all edges takes O(V^2) time

[wiki - adjacency matrix](https://en.wikipedia.org/wiki/Adjacency_matrix)
![adjacency matrix](./imgs/adjacency_matrix.png)

#### Adjacency List
- a way to represent a graph as a map from nodes to lists of edges.

*Pros*
- Space efficient for representing parse graphs.
- Iterating over all edges is efficient.

*Cons*
- Less space efficient for denser graphs.
- Edge weight lookup is O(E).
- Slightly more complex graph representation.

[wiki - adjacency list](https://en.wikipedia.org/wiki/Adjacency_list)
![adjacency list](./imgs/adjacency_list.png)

#### Edge List
- is a way to represent a graph as an unordered list of edges.
- the triplet (u, v, w) means: the cost from node u to bode v is w.
- it is seldomly used because of its lack of structure.
- it is conceptually simple and practical in a handful of algorithms.

*Pros*
- Space efficient for representing parse graphs.
- Iterating over all edges is efficient.
- very simple structure.

*Cons*
- Less space efficient for denser graphs.
- Edge weight lookup is O(E).

[wiki - edge list](https://en.wikipedia.org/wiki/Edge_list)
![edge list](./imgs/edge_list.png)


### Common Graph Theory Problems
<a id="top" href="#top">[Back to Top](#top)</a>

... directed or undirected?

... are edges weighted?

... is the graph sparse or dense with the edges?

... should I use an adjacency matrix, adjacency list, and edge list or other structure to represent the graph efficiently?


#### Shortest Path Problem
Given a weighted graph, find the shortest path of edges from node A to node B.

![shortest-path](./imgs/shortest_path_problem.png)

Algorithms: BFS(unweighted graph), Dijkstra's, Bellman-Ford, Floyd-Warshall, A*, and many more.

#### Connectivity
Does there exist a path between node A and node B?

![connectivity](./imgs/connectivity.png)

Solution: Use **union find** data structure or any search algorithm (e.d DFS)

#### Negative Cycles
Does my weighted digraph have any negative cycles? If so, where?

![negative-cycles](./imgs/negative_cycles.png)

Algorithms: Bellman-Ford and Floyd-Warshall

#### Strongly Connected Components (SCCs)
It can be thought of as self-contained cycles within a directed graph where every vertex in a given cycle can reach every other vertex in the same cycle.

![scc](./imgs/strongly-connected-components.png)

Algorithms: Tarjan's and Kosaraju's algorithm

#### Traveling Salesman Problem
The TSP problem is NP-Hard meaning it's a very computationally challenging problem. This is unfortunate because teh TSP has several very important applications.

![traveling salesman](./imgs/traveling_salesman_problem.png)

Algorithms: Held-Karp, branch and bound and many approximation algorithms

#### Finding Bridges in a Graph
A bridge / cut edge is any edge in a graph whose removal increase the number of connected components.

![bridges](./imgs/bridges.png)

Bridges are important in graph theory because they often hint at weak points, bottlenecks or vulnerabilities in a graph.

#### Articulation Points
An articulation point / cut vertex is any node in a graph whose removal increases the number of connected components.

![cut vertex](./imgs/cut_vertext.png)

#### Minimum Spanning  Tree (MST)
![MST-1](./imgs/mst_1.png)
![MST-2](./imgs/mst_2.png)

Algorithms: Kruskal's, Prim's & Boruvka's algorithm

#### Network flow: max flow
Q: With an infinite input source how much "flow" can we push through the network?

![network-flow](./imgs/network-flow.png)

Algorithms: Ford-Fulkerson, Edmonds-Karp & Dinic's algorithm

### Depth First Search
<a id="top" href="#top">[Back to Top](#top)</a>

DFS is the most fundamental search algorithm to explore nodes and edges of a graph.
- Time Complexity: O(V+E)
- It is used as a building block in other algorithms.
- By itself the DFS isn't all that useful.
- When augmented to perform other tasks such as count connected components, determine connectivity, or find the bridges/articulation points then DFS is very useful.

Basic DFS
: A DFS plunges depth first into a graph without regard for which edge it takes next until it cannot go any further at which point it backtracks and continues.

```python
# Global or class scope variables
n = num of nodes in the graph
g = adjacency list representing graph
visited = [False, ..., False] # size n

def dfs(at):
  if visited[at]:
    return
  visited[at] = True

  neighbors = graph[at]
  for next in neighbors:
    dfs(next)

# Start DFS at node 0
start_node = 0
dfs(start_node)
```

#### Use Case - Connected Components


