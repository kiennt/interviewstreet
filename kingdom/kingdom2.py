#!/usr/bin/env python
################################################################################
# Copyright 2012 Kien Nguyen Trung
# Filename: kingdom3.py
# Create: 2012/03/01
# Author: Nguyen Trung Kien (kiennt)
# Purpose:
#  
################################################################################

import sys
from collections import deque

sys.setrecursionlimit(15000)

class Graph:
  def __init__(self):
    self.size, m = [int(x) for x in raw_input().split()]

    self.incoming_nodes = {}
    self.outcoming_nodes = {}
    for i in range(0, self.size): 
      self.incoming_nodes[i+1] = []
      self.outcoming_nodes[i+1] = []
    for i in range(0, m): 
      x, y = [int(x) for x in raw_input().split()]
      self.outcoming_nodes[x].append(y)
      self.incoming_nodes[y].append(x)

class GraphAlgorithm:
  def __init__(self, graph):
    self.graph = graph
  
  def find_component_with_node(self, node):
    is_visited = [False] * (self.graph.size + 1)

    def visit(node):
      if is_visited[node]: return
      is_visited[node] = True
      for next_node in self.graph.incoming_nodes[node]:
        visit(next_node)
    
    visit(node)
    return is_visited

  def sort(self, in_component):
    incoming_nodes_size = [0]
    for node in range(1, self.graph.size + 1):
      incoming_nodes_size.append(len([n for n in self.graph.incoming_nodes[node] if in_component[n]]))

    topo_order = {}
    order = 0
    list_nodes = deque(node for node in range(1, self.graph.size+1) if not self.graph.incoming_nodes[node] and in_component[node])
    while list_nodes:
      node = list_nodes.popleft()
      topo_order[node] = order
      order += 1

      for next_node in self.graph.outcoming_nodes[node]:
        if in_component[next_node]:
          incoming_nodes_size[next_node] -= 1
          if incoming_nodes_size[next_node] == 0:
            list_nodes.append(next_node)

    return topo_order

  def solve(self, topo_order, in_component):
    connectivity = {}
    for node in topo_order.keys(): connectivity[(node, node)] = 1

    def cal(a, b):
      if (a, b) in connectivity: return connectivity[(a, b)]
      if topo_order[a] > topo_order[b]: 
        res = 0
      else:
        res = sum([cal(n, b) for n in self.graph.outcoming_nodes[a] if in_component[n]])
      connectivity[(a, b)] = res
      return res

    return cal(1, self.graph.size)

graph = Graph()
algo = GraphAlgorithm(graph)
in_component = algo.find_component_with_node(graph.size)
#print [x for x in range(1, graph.size + 1) if in_component[x]]
if not in_component[1]:
  print "0"
else:
  topo_order = algo.sort(in_component)
  #print topo_order
  if len(topo_order) < len([n for n in in_component if n]):
    print "INFINITE PATHS"
  else:
    print algo.solve(topo_order, in_component) % 1000000000
