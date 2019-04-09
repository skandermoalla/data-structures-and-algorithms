#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class UF:
    def __init__(self, nodes = []):
        self.nodes = nodes
        self.parent = {n:n for n in nodes}
        self.count = len(nodes)
        
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)
        if p1 == p2:
            return
        self.parent[p2] = p1
        self.count -= 1
