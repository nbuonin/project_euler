"""
Project Euler Problem #3
"""
from math import sqrt


def prime_tester(n):
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0):
            return False

    return True


def prime_generator(n):
    """Returns a list all primes less than n.
    Implements the sieve of Eratosthenes algo"""
    ints = [True for i in range(n + 1)]
    # Zero is not prime
    ints[0] = False

# For each integer from 1 to n, check if its prime.
# If so, then mark all multiples of that int as not prime
    for i in range(2, n + 1):
        if (ints[i] and prime_tester(i)):
            for j in range(i * 2, n + 1, i):
                ints[j] = False

    # 'sieve' out the primes
    return [i[0] for i in enumerate(ints) if i[1]]


def prime_factors(n):
    """Returns a list of prime factors"""
# First get a list of possible primes to check
    primes = prime_generator(int(sqrt(n)))
    factors = []
# 1 is always a factor so we don't need to include it
    for i in range(1, len(primes) - 1):
        while (n % primes[i] == 0):
            factors.append(primes[i])
            n = n / primes[i]

    return factors


def greatest_prime_factor(n):
    return prime_factors(n)[-1]


if __name__ == "__main__":
    print(greatest_prime_factor(600851475143))
