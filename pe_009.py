"""
Project Euler Problem #9
Pythogorian Triplet
"""
from functools import reduce


def pythagorian_checker(factors):
    return factors[0]**2 + factors[1]**2 == factors[2]**2


def sum_checker(factors, total):
    return sum(factors) == total


def pythagorian_triplet_checker(max_value):
    for x in range(1, max_value - 1):
        for y in range(2, max_value):
            z = max_value - x - y
            if (z > 0) and pythagorian_checker([x, y, z]):
                return (x, y, z)


if __name__ == "__main__":
    result = pythagorian_triplet_checker(1000)
    print("The triplet is: %d, %d, %d" % result)
    print("The product is %d" % reduce(lambda x, y: x * y, result))
