from math import gcd
from random import randint

def prime_factors(n):
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    for i in range(3, int(n**0.5)+1, 2):
        while n % i == 0:
            factors.add(i)
            n //= i
    if n > 2:
        factors.add(n)
    return list(factors)

def rho_pollard(n):
    if n % 2 == 0:
        return 2
    x, y, d = 2, 2, 1
    while d == 1:
        x = (x*x + 1) % n
        y = (y*y + 1) % n
        y = (y*y + 1) % n
        d = gcd(abs(x-y), n)
    return d

def get_prime_factors_rho(n):
    factors = []
    while n != 1:
        factor = rho_pollard(n)
        factors.extend(prime_factors(factor))
        while n % factor == 0:
            n //= factor
    return sorted(set(factors))

def is_ruth_aaron_pair(a, b):
    return sum(get_prime_factors_rho(a)) == sum(get_prime_factors_rho(b))

def ruth_aaron_pairs(start, end):
    last_sum = -1
    for i in range(start, end):
        current_sum = sum(get_prime_factors_rho(i))
        if current_sum == last_sum:
            if is_ruth_aaron_pair(i-1, i):
                print(i-1,i)
        last_sum = current_sum





while True:
    try:
        a, b = map(int, input().split())
        ruth_aaron_pairs(a,b)
    except EOFError:
        break


