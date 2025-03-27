# Task: Find Added

def find_added(st1, st2):
    return ''.join(sorted(s * (st2.count(s) - st1.count(s)) for s in set(st2)))


'''
# Best Solution:

## 1
from collections import Counter

def findAdded(st1, st2):
    return ''.join(sorted((Counter(st2) - Counter(st1)).elements()))

## 2
from collections import Counter

def findAdded(st1, st2):
    c = Counter(st2) - Counter(st1)
    return ''.join( k*c[k] for k in sorted(c.keys()) )

## 3    
def findAdded(st1, st2):
    return "".join(sorted(i * (st2.count(i)- st1.count(i)) for i in set(st2)))
'''