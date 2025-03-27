# Task: GA-DE-RY-PO-LU-KI cypher vol 3 - Missing key

def find_the_key(messages, secrets):
    s_key = set()
    s_messages = ''.join(messages)
    s_secrets = ''.join(secrets)
    for inx, msg in enumerate(s_messages):
        if msg != s_secrets[inx]:
            s_key.add([s_secrets[inx]+msg, msg+s_secrets[inx]][msg < s_secrets[inx]])
    return ''.join(sorted(s_key, key=lambda s: s[0]))


'''
# Best Solution:

## 1
def find_the_key(messages, secrets):
    return ''.join(sorted({a + b for a, b in map(sorted, zip(''.join(messages), ''.join(secrets))) if a != b}))

## 2
def find_the_key(*args):
    return ''.join(sorted({''.join(sorted((a,b))) for a,b in zip(*map(''.join, args)) if a!=b}))
'''