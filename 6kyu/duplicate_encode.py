# Task: Duplicate Encoder

from collections import Counter
def duplicate_encode(word):
    w = Counter(word.lower())
    return ''.join([ ')' if w.get(s) > 1 else '(' for s in word.lower()])


'''
# Best Solutions in codewars

# 1
def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])
'''