"""
Project Euler Problem #10
Give the sum of all primes less than two million
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
    # Zero and one are not prime
    ints[0] = False
    ints[1] = False

# For each integer from 1 to n, check if its prime.
# If so, then mark all multiples of that int as not prime
    for i in range(2, n + 1):
        if (ints[i] and prime_tester(i)):
            for j in range(i * 2, n + 1, i):
                ints[j] = False

    # 'sieve' out the primes
    return [i[0] for i in enumerate(ints) if i[1]]


def sum_of_primes(value):
    """ Returns the sum of all primes less than the value
    passed in. """
    return sum(prime_generator(value))


if __name__ == "__main__":
    print("The sum of all primes less than %d is %d"
          % (2000000, sum_of_primes(2000000)))
