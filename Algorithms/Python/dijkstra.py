# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 17:59:41 2019

@author: skand
"""

# =============================================================================
# Dijkstra's algorithm for shortest path from source
# implementing heapq library
# =============================================================================

import math
from heapq import *

class Graph:
    def __init__(self, nodes, edges):
        self.edges = edges
        self.nodes = nodes
        self.neighbours = {node:[] for node in self.nodes} 
        for u,v,w in edges:
            self.neighbours[u].append((v,w))
            self.neighbours[v].append((u,w))


def Dijkstra(G,s):
    tree = []
    q = []
    heapify(q)
    seen = set([s])
    for u, weight in G.neighbours[s]:
        heappush(q,(weight, (s,u)))
    
    while len(q) > 0:
        weight, edge = heappop(q)
        u,v = edge
        if v in seen: continue
        seen.add(v)
        tree.append((u,v,weight))
        for z, wz in G.neighbours[v]:
            heappush(q, (weight+wz, (v,z)))
    
    return tree

def test():
    nodes = ['a','b','e','f','s', 'c', 'g']
    edges = [('s','a',5),
             ('s','b',9),
             ('s','f',6),
             ('a','b',7),
             ('b','e',7),
             ('e','f',8),
             ('s','e',15),
             ('f','g',11),
             ('e','c',5),
             ('b','c',8),]
    G = Graph(nodes, edges)
    
    return Dijkstra(G,'s')
