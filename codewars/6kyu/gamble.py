# Task: Dreidel dreidel

import math
def gamble(rolls, my_coins, pot):
    for oper in rolls:
        if oper == "Nun":
            pass
        elif oper == "Gimel":
            my_coins += pot
            pot = 0
        elif oper == "Hei":
            my_coins += pot//2
            pot = (pot - pot//2)
        elif oper == "Shin":
            my_coins -= 1
            pot += 1
    return my_coins


'''
# Best Solution on codewars

# 1
def gamble(rolls, my_coins, pot):
    actions = {
	    "Nun":   lambda c, p: (c, p),
	    "Gimel": lambda c, p: (c + p, 0),
	    "Hei":   lambda c, p: (c + p//2, p - p//2),
	    "Shin":  lambda c, p: (c - 1, p + 1)
	    }
   
    c, p = my_coins, pot
    for roll in rolls:
        c, p = actions[roll](c,p)
    return c
    
'''