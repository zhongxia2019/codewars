# Task: Counting Duplicates

from collections import Counter

def duplicate_count(text):
    return len([ True for count in Counter(text.lower()).values() if count >=2 ])


'''
# Best Practices

## 1
def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])

'''