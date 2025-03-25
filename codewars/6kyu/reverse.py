# Task: Case Reversal of Consecutive Duplicates

def reverse(st):
    inx = 0
    while inx <= len(st)-1:
        step = 1
        while inx+step < len(st) and st[inx] == st[inx+step]:
            step += 1
        if step >= 2:
            st = st[:inx] + [step*st[inx].upper(), step*st[inx].lower()][st[inx].isupper()] + st[inx+step:]
        inx = inx + step
    return st


'''
# Best Solution:

## 1
import re

def reverse(s):
    return re.sub(r'(.)\1+', lambda m: m.group().swapcase(), s)

## 2
from itertools import groupby as gr
def reverse(s):
    a = [''.join(g) for n,g in gr(s)]
    return ''.join(i if len(i)==1 else i.swapcase() for i in a)
'''