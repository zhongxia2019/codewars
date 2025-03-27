# Task：Free pizza

def pizza_rewards(customers, min_orders, min_price):
    free_pizza = set()
    for name, orders in customers.items():
        if list(map(lambda x: x >= min_price , orders)).count(True) >= min_orders:
            free_pizza.add(name)
    return free_pizza


'''
# Best Solution:

## 1
def pizza_rewards(customers, min_orders, min_price):
    return {customer for customer, orders in customers.items() if sum(1 for order in orders if order >= min_price) >= min_orders}
    
'''