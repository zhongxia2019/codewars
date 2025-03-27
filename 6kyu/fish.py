# Task: Plenty of Fish in the Pond

def fish(shoal):
    if len(shoal) == 0:
        return 1
    size, extra = 1, 0
    for fish in sorted(map(int, shoal[:])):
        if size>= fish:
            extra += fish
        if extra >= 4*size:
            extra -= 4*size
            size += 1
    return size


