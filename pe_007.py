"""
Project Euler Problem #7
Give the 10001st prime
"""
from math import sqrt


def prime_tester(n):
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0):
            return False

    return True


def nth_prime(n):
    """Returns the nth prime"""
    i = 2
    primes = []
    while len(primes) < n:
        if prime_tester(i):
            primes.append(i)

        i += 1

    return primes[-1]


if __name__ == "__main__":
    print(nth_prime(10001))
