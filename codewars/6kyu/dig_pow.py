# Task: Playing with digits

def dig_pow(n, p):
    np = sum( pow(int(s),i+p) for i,s in enumerate(str(n)) )
    return np / n if np % n == 0 else -1