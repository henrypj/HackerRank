# Returns all factors of a given number n
import functools

def factors(n):    
    return set(functools.reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

print(factors(96))