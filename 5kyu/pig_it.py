# Task: Simple Pig Latin

import string

def pig_it(text):
    return ' '.join([s if (s in string.punctuation) else s[1:] + s[0] + "ay" for s in text.split()])


'''
# Best Practice:

## 1
def pig_it(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())
'''