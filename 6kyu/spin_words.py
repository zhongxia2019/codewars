# Task: Stop gninnipS My sdroW!

def spin_words(sentence):
    s_space = sentence.split(' ')
    if len(s_space) <= 1:
        return s_space[0] if len(s_space[0]) < 5 else s_space[0][::-1]
    return ' '.join([s if len(s)<5 else s[::-1] for s in s_space])


'''
# Best Practice:

## 1
def spin_words(sentence):
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
'''