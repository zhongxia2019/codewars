# Task: Moving Zeros To The End

def move_zeros(lst):
    lst_zero = [ lst.pop(inx) for inx in range(len(lst)-1,-1,-1) if lst[inx] == 0 ]
    return lst + lst_zero


'''
# Best Practice:

## 1
def move_zeros(array):
    return [x for x in array if x] + [0]*array.count(0)

## 2
def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))

## 3
def move_zeros(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)

    
'''