# Task: Word a10n (abbreviation)

import re

def abbreviate(s):
    word4len = lambda x: [x, x[0] + str(len(x)-2) + x[-1]][len(x)>=4]
    res = [word4len(x) for x in re.split('([^a-zA-Z]+)', s) if x]
    return ''.join(res)


'''
# Best Solutions in codewars

## 1
import re

regex = re.compile('[a-z]{4,}', re.IGNORECASE)

def replace(match):
    word = match.group(0)
    return word[0] + str(len(word) - 2) + word[-1]

def abbreviate(s):
    return regex.sub(replace, s)

## 2
def abbreviate(s):
    mutate = lambda w: w[0] + str(len(w) - 2) + w[-1] if len(w) > 3 else w
    result, word = '', ''
    for char in s:
        if char.isalpha():
            word += char
        else:
            result += mutate(word) + char
            word = ''
    result += mutate(word)
    return result    

'''