"""
Project Euler Problem #2
Give the sum of the even Fibonacci numbers
for those Fibonacci's less than four million
"""


def fib(max_val):
    a = 0
    b = 1
    while ((a + b) < max_val):
        yield a + b
        c = a
        a = b
        b += c


if __name__ == "__main__":
    print(sum([i for i in fib(4000000) if (i % 2 == 0)]))
