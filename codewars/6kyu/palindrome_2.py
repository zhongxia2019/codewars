# Task: Numerical Palindrome #4

def palindrome(num):
    if type(num) is not int or num < 0:
        return 'Not valid'
    x = 0 if num >= 11 else 11-num
    while True:
        if str(num+x) == str(num+x)[::-1]:
            return num+x
        if str(num-x) == str(num-x)[::-1]:
            return num-x
        x += 1


'''
# Best Solutions in codewars

## 1
def palindrome(num):
    is_palindrome = lambda chunk: int(chunk) > 9 and chunk == chunk[::-1]
    if not isinstance(num, int) or num < 0: return 'Not valid'
    i = 0
    while(True):
        if is_palindrome(str(num + i)): return num + i
        if is_palindrome(str(num - i)): return num - i
        i += 1
        
'''        