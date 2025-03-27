# Task: Longest Mountain Pass


'''
# Best Solution in codewars

# 1
def longest_mountain_pass(mountains, E):
    costs = [max(0, b - a) for a, b in zip(mountains, mountains[1:])]
    idx = i = 0
    print(costs)
    for e in costs:
        E -= e
        print('start', i, idx, E, e)
        if E >= 0:
            idx = i
        else:
            E += costs[i]
            i += 1
        print('end  ', i, idx, E, e)
    return (len(mountains) - i, idx)

# 2
def longest_mountain_pass(mountains, E):
    n = len(mountains)
    if n < 2:
        if n == 0 :
            return (0, 0)
        else: return (1, 0)

    # Precompute energy costs
    energy_cost = [0] * n
    for i in range(1, n):
        energy_cost[i] = max(0, mountains[i] - mountains[i - 1]) + energy_cost[i - 1]

    # Sliding window
    max_length = 0
    start_index = 0
    left = 0
    for right in range(n):
        while energy_cost[right] - (energy_cost[left] if left > 0 else 0) > E:
            left += 1
        if right - left + 1 > max_length:
            max_length = right - left + 1
            start_index = left

    return (max_length, start_index)    
'''
