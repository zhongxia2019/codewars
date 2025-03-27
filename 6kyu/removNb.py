# Task: Is my friend cheating?


def remov_nb(n):
    res = []
    total = (1+n) * n / 2
    for x in range(1, n+1):
        y = (total - x) / (x+1)
        if y-int(y) == 0 and y <= n:
            res.append((x, int(y)))
    return res
