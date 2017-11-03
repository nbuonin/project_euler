"""
Project Euler Problem #1
Give the sum of all the multiples of either 3 or 5 for all natural
numbers less than 1000
"""


def sum_multiples_of_three_and_five(val):
    return sum([i for i in range(val) if ((i % 3 == 0) or (i % 5) == 0)])


if __name__ == "__main__":
    print(sum_multiples_of_three_and_five(1000))
