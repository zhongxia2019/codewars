# Task: Triangle of Multiples (Easy One)

def mult_triangle(n):
    total_sum = sum( x**3 for x in range(1,n+1))
    total_odd_sum = ((n+1) // 2)**4
    return [total_sum, total_sum-total_odd_sum, total_odd_sum]


'''
# Best Parctices

## 1
def mult_triangle(n):
    total = (n * (n + 1) / 2)**2
    odds = ((n + 1) // 2)**4
    return [total, total - odds, odds]
'''