"""
Project Euler Problem #6
Give the difference of the sum the first hundred natural
numbers and the square of the sum of the first hundred natural numbers.
"""


def sum_square_diff(n):
    sum_n = sum([i**2 for i in range(n + 1)])
    square = sum([i for i in range(n + 1)])**2
    return square - sum_n


if __name__ == "__main__":
    print(sum_square_diff(100))
