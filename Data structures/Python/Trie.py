# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 18:28:08 2019

@author: skand
"""
class Node:
    def __init__(self, children = {}):
        self.children = children
        self.isWord = False
        
class Trie:
    def __init__(self):
        self.head = Node()
        
    def insert(self, word):
        curr = self.head
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]
        curr.isWord = True
        
    def find(self, word):
        curr = self.head
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.isWord
    
    def auto_complete(self, pref):
        res = []
        curr = self.head
        for char in pref:
            if char not in curr.children:
                return res
            curr = curr.children[char]
        #at the root of all possible words starting with pref
        stack = [(curr, pref)]
        while len(stack) > 0:
            curr, pref = stack.pop()
            if curr.isWord:
                res.append(pref)
            for char, child in curr.children.items():
                stack.append((child, pref + char))
        return res