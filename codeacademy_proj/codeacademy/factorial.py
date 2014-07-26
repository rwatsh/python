__author__ = 'rushil'
def factorial(x):
    if x == 1:
        return 1
    fact = 1
    for i in range(1, x+1):
        fact *= i
    return fact

print factorial(2)