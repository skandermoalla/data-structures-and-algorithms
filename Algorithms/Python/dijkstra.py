# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 17:59:41 2019

@author: skand
"""

# =============================================================================
# Dijkstra's algorithm for shortest path from source
# implementing heapq library
# =============================================================================

class Graph:
    def __init__(self, edges = []):
        self.nodes = set()
        self.edges = edges
        for edge in edges:
            self.nodes.add(edge[0])
            self.nodes.add(edge[1])
        self.next = {n:set() for n in self.nodes}
        for edge in edges:
            self.next[edge[0]].add((edge[1], edge[2]))
            self.next[edge[1]].add((edge[0], edge[2]))
        
        
def Dijkstra(g, s):
    dist = {}
    res = []
    seen = set()
    q = []
    heapq.heapify(q)
    for node in g.nodes:
        if node != s:
            heapq.heappush(q, (math.inf, node, None))
            dist[node] = math.inf
        else:
            heapq.heappush(q, (0, s, None))
            dist[s] = 0
            
    while len(q) > 0:
        cur_dist, u, pred = heapq.heappop(q)
        if u in seen: continue
        seen.add(u)
        res.append((pred, u, cur_dist))
        for v, edge_dist in g.next[u]:
            if v in seen: continue
            if (cur_dist + edge_dist) < dist[v]:
                dist[v] = cur_dist + edge_dist
                heapq.heappush(q, (dist[v], v, u))
    return res

def test():
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
    G = Graph(edges)
    
    return Dijkstra(G,'s')
