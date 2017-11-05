"""
Project Euler Problem #5
Give the smallest number that can be divided evenly by all
integers 1 - 20
"""


def div_checker(n, max_range):
    for i in range(1, max_range + 1):
        if n % i > 0:
            return False

    return True


def smallest_multiple(n):
    """Finds the smallest integer that is evenly divisible by all ints
    less than n"""
    found = False
    i = n + 1
    while not found:
        if div_checker(i, n):
            return i
        i += 1


if __name__ == "__main__":
    print("Smallest Multiple: %d" % smallest_multiple(20))
