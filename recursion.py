def recur_power(n):
    """
    (int) -> int

    returns the power of the number based on the dependence
    n^2 = (n-1)^2 + 2 (n-1) +1
    if argument isn't positive or integer return None
    :argument positive integer
    :return integer
    """
    try:
        assert (isinstance(n, int))
        assert (n > 0)

        if n == 1:
            return 1

        return recur_power(n - 1) + 2 * (n - 1) + 1

    except AssertionError:
        print("Argument(n) should be positive integer")
        return None

# print(recur_square())

def recur_sum(n, m):
    """
    (int, int) -> int

    returns the sum of the range 1 ^ m + 2 ^ m + ... + n ^ m
    if argument isn't positive return None
    :arguments positive numbers
    :return integer
    """
    try:
        assert (n > 0 and m > 0)

        if n == 1:
            return 1

        return n ** m + recur_sum(n - 1, m)

    except AssertionError:
        print("Arguments(n and m) should be positive numbers")
        return None


# print(recur_sum(4, 1))


def recur_divisor(n, m):
    """
    (int, int) -> int

    returns the largest common divisor for the numbers based
    on the dependence F (n, m) = F (n-m, m), if n> m;
                      F (n, m) = F (n, m-n) if n <m.
    if argument isn't positive or integer return None
    :argument positive integers
    :return integer
    """
    try:
        assert (isinstance(n, int))
        assert (isinstance(m, int))
        assert (n > 0 and m > 0)

        if n == m:
            return n

        if n > m:
            return recur_divisor(n - m, m)
        if n < m:
            return recur_divisor(n, m - n)

    except AssertionError:
        print("Arguments(n and m) should be positive integers")
        return None


# print(recur_divisor(343, 98))


def recur_list(st, a=0, b=0):
    """
    (int, int) -> int

    returns a list of two numbers in which the first number is
    the number of capital letters in a row and the second is
    the number of lowercase letters in a row
    if argument isn't positive or integer return None

    :argument positive integers
    :return integer
    """
    try:
        assert (isinstance(st, str))

        if not st:
            return [a, b]

        if ord(st[-1]) in range(65, 91):
            return recur_list(st[:-1], a + 1, b)
        elif ord(st[-1]) in range(97, 123):
            return recur_list(st[:-1], a, b + 1)
        else:
            return recur_list(st[:-1], a, b)

    except AssertionError:
        print("Argument should be string")
        return None

# print(recur_list('sofij8430h))*f8h09wf'))
