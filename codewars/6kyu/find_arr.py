# Task: Find a Bunch of Common Elements of Two Lists in a Certain Range

from collections import Counter

def find_arr(arr_a, arr_b, rng, wanted):
    set_a = { val for val,count in Counter(arr_a).items() if count >= 2 }
    set_b = { val for val,count in Counter(arr_b).items() if count >= 2 }
    set_repeat = set_a & set_b
    res = []    
    for val in set_repeat:
        if rng[0] <= val <= rng[1] and \
            ((wanted == "odd" and val % 2 in (-1,1)) or (wanted == "even" and val % 2 == 0)):
            res.append(val)
    return sorted(res)


'''
# Best Practices

## 1
from collections import Counter

def find_arr(arrA, arrB, rng, wanted):
    ca, cb = Counter(arrA), Counter(arrB)
    m, n = rng
    m += (m % 2 == 1) == (wanted == 'even')
    r = range(m, n+1, 2)
    return [v for v in r if ca[v] > 1 and cb[v] > 1]


## 2
from collections import Counter

def find_arr(arrA, arrB, rng, wanted):
    cntr = Counter(arrA) & Counter(arrB)
    return sorted(k for k, v in cntr.items() if v >= 2 and rng[0] <= k <= rng[1] and k % 2 == (wanted == 'odd'))


## 3
from collections import Counter

def find_arr(arrA, arrB, rng, wanted):
    (low, upp), parity = rng, (wanted == 'odd')
    C1 = Counter(x for x in arrA if low <= x <= upp and x&1 == parity)
    C2 = Counter(x for x in arrB if low <= x <= upp and x&1 == parity)
    return sorted(x for x in C1.keys() & C2.keys() if C1[x] > 1 < C2[x])
'''