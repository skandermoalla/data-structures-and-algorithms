# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 13:52:36 2018

@author: skand
"""

# =============================================================================
# Binary Search Tree
# implements:
#   - find(key) // O(height) best case O(logn) worst case O(n)
#   - insert(key) O(height) best case O(logn) worst case O(n)
#             // tweak for insertion of repetitive keys
#   - inorder //  O(n)
 
# =============================================================================

class Node:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right
        
        
class BST:
    def __init__(self):
        self.root = None
        
    def find(self, key):
        return self._find(self.root, key)
        
    def _find(self, node, key):
        if node is None:
            return False
        if node.key == key:
            return True
        elif key > node.key:
            return self._find(node.right, key)
        else:
            return self._find(node.left, key)
        
    def insert(self, key):
        self.root = self._insert(self.root, key)
        
    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node
            
    def inorder(self):
        res = []
        if self.root is None:
            return
        cur = self.root
        stack = [cur]
        right = True
        while len(stack) > 0:
            if right:
                while cur.left is not None:
                    cur = cur.left
                    stack.append(cur)
            cur = stack.pop()
            res.append(cur.key)
            if cur.right is not None:
                cur = cur.right
                stack.append(cur)
                right = True
            else:
                right = False
        return res
    
    def inorder_recursive(self):
        res = []
        self._inorder_recursive(self.root, res)
        return res
    
    def _inorder_recursive(self, cur, res):
        if cur == None:
            return
        self._inorder_recursive(cur.left, res)
        res.append(cur.key)
        self._inorder_recursive(cur.right, res)
        
    def delete(self, key):
        cur = self.root
        prv = None
        direc = 0 #0 if left else 1
        while (cur is not None) and cur.key != key:
            if key > cur.key:
                cur, prv, direc = cur.right, cur, 1
            else:
                cur, prv, direc = cur.left, cur, 0
        if cur is None:
            return
        if direc:
            prv.right = self._delete(cur)
        else:
            prv.left = self._delete(cur)
            
    def _delete(self, cur):
        if cur.left == None:
            return cur.right
        elif cur.right == None:
            return cur.left
        else:
            # both right and left are not None
            # get max on left of cur
            tmp = cur.left
            prv = None
            while tmp.right is not None:
                tmp, prv = tmp.right, tmp
            if prv is not None:
                prv.right = None
            else:
                cur.left = None
            tmp.right = cur.right 
            tmp.left = cur.left
            return tmp
                
                
            
            
        
    
def test1():
    t = BST()
    for key in [5,3,2,1,4,7,12,9,14,8,11,6]:
        t.insert(key)
    return t