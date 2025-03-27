# Task: Numerical Palindrome #1.5

def palindrome(num, s):
    if type(num) is not int or type(s) is not int or num < 0 or s < 0:
        return 'Not valid'
    x, res = max(num, 11), []
    while len(res) < s:
        if str(x) == str(x)[::-1]:
            res.append(x)
        x += 1
    return res