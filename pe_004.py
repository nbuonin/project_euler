"""
Project Euler Problem #4
Find the largest pallindrome of two three digit numbers
"""


def p_tester(n):
    """tests if passed value is a pallindrome"""
    test_str = list(str(n))
    test_str_rev = list(test_str)
    test_str_rev.reverse()
    return test_str == test_str_rev


class ProductKeeper:
    """An object test and track the largest pallindrome"""
    def __init__(self):
        self.greatest_pallindrome = 0
        self.prod_a = 0
        self.prod_b = 0

    def check(self, p, q):
        prod = p * q
        if p_tester(prod) and prod > self.greatest_pallindrome:
            self.greatest_pallindrome = prod
            self.prod_a = p
            self.prod_b = q

    def get_gp(self):
        return (self.greatest_pallindrome,
                self.prod_a,
                self.prod_b)


def greatest_pallindrome(n, m):
    """
    Check all distinct pairs of integers within a range
    for the largest product which is also a pallindrome.
    returns a tuple of the form: (product, factor, factor)
    """
    if m < n:
        raise ValueError

    pk = ProductKeeper()

    # these nested loops compare distinct pairs of products
    for i in range(n + 1, m + 1):
        for j in range(n, i):
            pk.check(i, j)

    return pk.get_gp()


if __name__ == "__main__":
    print("The largest pallindrome: %d, its factors are: %d, %d"
          % greatest_pallindrome(100, 999))
