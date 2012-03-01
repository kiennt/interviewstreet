#!/usr/bin/env python
import sys
sys.setrecursionlimit(15000)

class Graph:
  def __init__(self):
    self.size, m = [int(x) for x in raw_input().split()]
    self.incomming_nodes = {}
    self.outcomming_nodes = {}
    for n in range(1, self.size + 1): 
      self.incomming_nodes[n] = []
      self.outcomming_nodes[n] = []
    for i in range(1, m + 1):
      x, y = [int(x) for x in raw_input().split()]
      self.incomming_nodes[y].append(x)
      self.outcomming_nodes[x].append(y)

  def dfs(self, start_node, end_node):
    in_path = [False] * (self.size + 1)
    count = [0] * (self.size + 1)
    self.stop_recusive = False

    def visit(node):
      if count[node] == -1: return
      count[node] = -1
      for next_node in self.outcomming_nodes[node]:
        visit(next_node)

    def count_path(node):
      if self.stop_recusive: return -1
      if count[node] > -1: return count[node]

      in_path[node] = True
      count[node] = 0

      for next_node in self.incomming_nodes[node]:
        if in_path[next_node]:
          self.stop_recusive = True
          return -1
        else:
          count[node] += count_path(next_node)

      in_path[node] = False
      return count[node]
   
    visit(end_node)
    count[end_node] = 1
    count_path(start_node)
    if self.stop_recusive:
      print "INFINITE PATHS"
    else:
      print count[start_node] % 1000000000

graph = Graph()
graph.dfs(graph.size, 1)
