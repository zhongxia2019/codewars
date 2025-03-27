# Task: Return 1, 2, 3 randomly

import time
def one_two_three():
    t = int(str(time.time()).replace('.', ''))
    i = id(t)
    return (t^i) % 3 + 1


'''
# Best Solutions in codewars

## 1
def one_two_three():
    res = one_two(), one_two()
    return ( 1 if res == (1, 1) else
             2 if res == (1, 2) else
             3 if res == (2, 1) else
             one_two_three() )

## 2
one_two_three = lambda: 2 * one_two() + one_two() - 3 or one_two_three()             
'''