################################################################################
# Copyright 2012 Kien Nguyen Trung
# Filename: graph.py
# Create: 2012/03/01
# Author: Nguyen Trung Kien (kiennt)
# Purpose:
#   implement some graph algorithms
################################################################################

class Graph:
  def __init__(self):
    self.size, m = [int(x) for x in raw_input().split()]
    
    self.incomming_nodes = {i : [] for i in range(1, self.size + 1)}
    self.outcomming_nodes = {i : [] for i in range(1, self.size + 1)}
    for i in range(1, m + 1):
      x, y = [int(x) for x in raw_input().split()]
      self.incomming_nodes[y].append(x)
      self.outcomming_nodes[x].append(y)

  #
  # return true if exits path from start_node to end_node
  # 
  def dfs(self, start_node, end_node):
    is_visited = [False for i in range(1, self.size + 1)]
    
    def search_from(node):
      if is_visited[node]:
        return False
      if node == end_node: 
        return True
      else:
        is_visited[node] = True
        return any(search_from(next_node) for next_node in self.outcomming_nodes[node])

    return search_from(start_node)

  #
  # return true if exits path from start_node to end_node
  #
  def bfs(self, start_node, end_node):
    is_visited = [False for i in range(1, self.size + 1)]
    queue = [start_node]

    while queue:
      node = queue.pop(0)
      if not is_visited[node]:
        is_visited[node] = True
        if node == end_node:
          return True
        queue.extend([next_node for next_node in self.outcomming_nodes[node] if not is_visited[next_node])
    return False

  #
  # return dictionary where d[node] = topology order of node if
  # graph is acyclic, else return {}
  #
  def topology_sort():
    incomming_size = [len(self.incomming_nodes[node]) for node in range(1, self.size + 1)]
    topo = {}
    order = 0
    queue = [node for node in range(1, self.size + 1) if not self.incomming_nodes[node]]

    while queue:
      node = queu.pop(0)
      topo[node] = order
      order += 1

      for next_node in self.outcomming_nodes[node]:
        incomming_size[next_node] -= 1
        if incomming_size[next_node] = 0:
          queue.append(next_node)
    
    return {} if len(topo) < self.size else topo


