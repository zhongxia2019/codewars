# Task: Find the odd int

def find_it(seq):
    for x in set(seq):
        if seq.count(x) % 2 !=0:
            return x
    return None