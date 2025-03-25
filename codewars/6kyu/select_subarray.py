# Task: Remove a Specific Element of an Array

import math

def select_subarray(arr):
    sub_arr = [ arr[:i] + arr[i+1:] for i in range(len(arr))]
    inx_q = map(lambda x: [x[0], abs(math.prod(x[1]) / sum(x[1]))], [[inx,s] for inx, s in enumerate(sub_arr) if sum(s)!=0])
    inx_q = sorted(list(inx_q), key=lambda x: x[1])
    inx_list = [ inx for inx, q in inx_q if q == inx_q[0][1] ]
    res = []
    for inx in inx_list:
        sub_arr_set = set(sub_arr[inx])
        val = list(set(arr)-sub_arr_set)[0]
        res.append([arr.index(val), val])
    return res if len(res) >= 2 else res[0]


'''
# Best Solution:

## 1
import math

def select_subarray(arr):
    total = sum(arr)
    prod = math.prod(arr)
    q_inx = sorted([[abs( (prod/x) / (total-x) ), inx] for inx, x in enumerate(arr) if total-x!=0])
    res = [ [inx, arr[inx]] for q, inx in q_inx if q == q_inx[0][0] ]
    return res if len(res) >= 2 else res[0]

## 2
from heapq import nsmallest

def select_subarray(arr):
    s = sum(arr)
    (v1, c1, a1), (v2, c2, a2) = nsmallest(2, ((-abs(a * (s - a)), c , a) for c, a in enumerate(arr)))
    return [[c1, a1], [c2, a2]] if v1 == v2 else [c1, a1]
'''