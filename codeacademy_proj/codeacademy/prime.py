__author__ = 'rushil'
def is_prime(x):
    if x == 0 or x == 1 or x < 0:
        return False
    for n in range(2, x-1):
        if x%n == 0:
            return False
    return True

print is_prime(-10)
print is_prime(0)
print is_prime(13)
print is_prime(6)