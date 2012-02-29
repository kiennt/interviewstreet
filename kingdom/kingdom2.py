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
sys.setrecursionlimit(15000)

class Graph:
  def __init__(self):
    self.size, m = [int(x) for x in raw_input().split()]

    self.incoming_edges = {}
    self.outcoming_edges = {}
    for i in range(0, self.size): 
      self.incoming_edges[i+1] = []
      self.outcoming_edges[i+1] = []
    for i in range(0, m): 
      x, y = [int(x) for x in raw_input().split()]
      self.outcoming_edges[x].append(y)
      self.incoming_edges[y].append(x)

class GraphAlgorithm:
  def __init__(self, graph):
    self.graph = graph

  def find_component_for(self, anode):
    nodes_visited = [False] * (self.graph.size + 1)
    component = [] 
    def visit(node):
      if nodes_visited[node]: return
      nodes_visited[node] = True
      component.append(node)
      for n in graph.incoming_edges[node]: visit(n) 

    visit(anode)
    return component

  def sort(self, nodes):
    topo_order = {}
    order = 0
    list_roots = [node for node in nodes if not self.graph.incoming_edges[node]]
    if not list_roots: return {} # has circle
    root = list_roots[0]

    while True:
      topo_order[root] = order
      order += 1
      if order == len(nodes): break
      
      next_node = root
      for node in self.graph.outcoming_edges[root]:
        if all(n in topo_order for n in self.graph.incoming_edges[node]):
          next_node = node
          break
      if next_node == root: return {} # has circle
      root = next_node

    return topo_order
  
  def solve(self, topo_order):
    connectivity = {}
    for node in topo_order.keys(): connectivity[(node, node)] = 1

    def cal(a, b):
      if (a, b) in connectivity: return connectivity[(a, b)]
      if topo_order[a] > topo_order[b]: 
        res = 0
      elif self.graph.incoming_edges[b] == [a]:
        res = 1
      else:
        res = sum([cal(n, b) for n in self.graph.outcoming_edges[a]])
      connectivity[(a, b)] = res
      return res

    return cal(1, self.graph.size)

graph = Graph()
algo = GraphAlgorithm(graph)
component = algo.find_component_for(graph.size)
if 1 not in component:
  print "0"
else:
  topo_order = algo.sort(component)
  if not topo_order: 
    print "INFINITE PATHS"
  else:
    print algo.solve(topo_order)
