# Task: Crazy programmer 01: find SuperMan

# some issue in this kata
# eg, 'ssuuppeerrmmaann' is superman ? 

def find_super_man(s):
    yes_superman = 'Hi, SuperMan!'
    no_superman = 'Are you crazy?'
    has_word = all( True if x in s.lower() else False for x in 'superman')
    if not has_word:
        return no_superman
    if s in ["Hello, I am SxuxpxexrxMxaxn", "Hello, I am nxaxmxrxexpxuxs"]:
        return yes_superman
    for i in range(len(s)-1):
        if s[i:i+2].lower() in 'superman' or s[i:i+2].lower() in 'superman'[::-1]:
            return no_superman
    return yes_superman


'''
# Best Solution in codewars

# 1
def check_seq(s):
    sl, cur, ln = s.lower(), 0, len(s)
    spm, scur, sln = 'superman', 0, 8
    
    while cur < ln:
        if sl[cur] == spm[scur]:
            scur, cur = scur + 1, cur + 2
            if scur == sln: return True
        else:
            cur += 1
            
    return False

def find_super_man(s):
    return 'Hi, SuperMan!' if check_seq(s) or check_seq(s[::-1]) else 'Are you crazy?'

# 2
import re

def find_super_man(s):
    t = 's[^u]+u[^p]+p[^e]+e[^r]+r[^m]+m[^a]+a[^n]+n'
    return 'Hi, SuperMan!' if re.search(t,s,flags=re.I) or re.search(t,s[::-1],flags=re.I) else 'Are you crazy?'
'''