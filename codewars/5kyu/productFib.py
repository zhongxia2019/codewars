# Task: Product of consecutive Fib numbers

def product_fib(_prod):
    if _prod == 0:
        return [0 ,1, True] 
    fibo = [0, 1]
    for i in range(_prod):
        fibo.append(fibo[-2] + fibo[-1])
        if fibo[-2]*fibo[-1] == _prod:
            return [fibo[-2], fibo[-1], True]
        elif fibo[-1]*fibo[-2] > _prod:
            return [fibo[-2], fibo[-1], False]


'''
# Best Solutions in codewars

## 1
def productFib(prod):
  a, b = 0, 1
  while prod > a * b:
    a, b = b, a + b
  return [a, b, prod == a * b]

'''