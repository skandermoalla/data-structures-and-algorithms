# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 13:19:36 2018

@author: skand
"""

# =============================================================================
# A balanced min heap represented by a list [None, (root), ...,...]
# indexes of children are 2*index_parent and 2*index_parent+1
# index of rapent is index_child // 2
# insertion is O(log(n)) #for fixup
# pop_min is O(log(n)) # for fixdown 
# =============================================================================
class Heap:
    def __init__(self):
        self.rep = [None]
        
    def size(self):
        return len(self.rep) - 1
    
    def exchange(self, p1, p2):
        self.rep[p1], self.rep[p2] = self.rep[p2], self.rep[p1]
        
    def insert(self, key):
        self.rep.append(key)
        self.fixup(self.size())
        
    def fixup(self, pos):
        if pos == 1: return
        parent = pos // 2
        if self.rep[parent] > self.rep[pos]:
            self.exchange(parent, pos)
            self.fixup(parent)
            
    def pop_min(self):
        if self.size() == 0:
            return
        if self.size() == 1:
            return self.rep.pop()
        
        m = self.rep[1]
        self.rep[1] = self.rep.pop()
        self.fixdown(1)
        return m
    
    def fixdown(self, pos):
        if pos >= self.size():
            return
        if 2*pos <= self.size():
            if 2*pos+1 <= self.size():
                m = min(2*pos, 2*pos+1, key = lambda x: self.rep[x])
                if self.rep[pos] <= m: return
                self.exchange(pos, m)
                self.fixdown(m)
            else:
                if self.rep[pos] <= self.rep(2*pos): return
                self.exchange(pos, 2*pos)
                self.fixdown(2*pos)