# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 11:53:16 2018

@author: skand
"""
import math
import random

def binary_search(key, l, start = 0, end = math.inf):
    """
    searches in a sorted array in the binary style
    """
    end = min(len(l), end)
    while  start < end:
        mid = (start + end) //2
        if l[mid] == key:
            return mid
        elif key > l[mid]:
            start = mid+1
        else:
            end = mid
    return False
    
    
def binary_search_recursive(key, l, start, end):
    if start >= end:
        return False
    mid = (start+end)//2
    if key == l[mid]:
        return mid
    elif key < l[mid]:
        return binary_search_recursive(key, l, start, mid)
    else:
        return binary_search_recursive(key, l, mid+1, end)
    
def insertion_sort(l):
    if len(l) < 2:
        return l
    for key_index in range(1, len(l)):
        key = l[key_index]
        j = key_index-1
        while j >= 0 and l[j] > key:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key
    return l

def partition(l, st, ed):
    p = l[st]
    i = st+1
    j = ed-1
    while True:
        while i < ed and l[i] <= p:
            i+=1
        while j > st and l[j] > p:
            j-=1
        if i >= j:
            break
        l[i], l[j] = l[j], l[i]
        
    l[st], l[j] = l[j], l[st]
    return j
            
def quicksort(l):
    random.shuffle(l)
    quicksort_helper(l, 0, len(l))
    
def quicksort_helper(l, st, ed):
    if ed <= st+1: return
    p = partition(l, st, ed)
    quicksort_helper(l, st, p)
    quicksort_helper(l, p+1, ed)    
    
        
    
