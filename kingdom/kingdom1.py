#!/usr/bin/env python
import sys
sys.setrecursionlimit(15000)

class Graph:
  def __init__(self):
    self.n, m = [int(x) for x in raw_input().split()]
    self.edges = {}
    for i in range(0, self.n): self.edges[i+1] = set()
    for i in range(0, m): 
      x, y = [int(x) for x in raw_input().split()]
      self.edges[x].add(y)


class DFS:
  def __init__(self, graph):
    self.graph = graph
    self.circle = [False] * (self.graph.n + 1)
 
  def search(self, start_node, end_node):
    path = [start_node]
    nodes_visited = [False] * (self.graph.n + 1)
    nodes_visited[start_node] = True
    connectivity = [0]
    stop_recursive = [False]

    def search_from(node, find_circle):
      if stop_recursive[0]: return

      if not find_circle and node == end_node:
          if any(self.circle[n] for n in path): 
            connectivity[0] = -1
            stop_recursive[0] = True
            return
          connectivity[0] += 1
      else:
        for n in self.graph.edges[node]:
          if not nodes_visited[n]:
            nodes_visited[n] = True
            path.append(n)
            search_from(n, find_circle)
            path.pop()
            nodes_visited[n] = False
          elif find_circle:
              reverse_path = path[::-1]
              for x in reverse_path[0:reverse_path.index(n)+1]: 
                self.circle[x] = True
  
    search_from(start_node, True)
    search_from(start_node, False)
    if connectivity[0] != -1:
      print connectivity[0]
    else:
      print 'INFINITE PATHS'
     
g = Graph()
dfs = DFS(g)
dfs.search(1, g.n) 
