import math
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True



"""
print(is_prime(7))
print(math.sqrt(10))
print(int(math.sqrt(10)))
"""