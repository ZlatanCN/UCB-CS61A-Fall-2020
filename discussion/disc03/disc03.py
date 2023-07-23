def multiply(m, n):
    """
    >>> multiply(5, 3)
    15
    """
    if n == 1:
        return m
    else:
        return m + multiply(m, n - 1)


def hailstone(n, cnt=0):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    if n == 1:
        cnt += 1
        print(int(n))
        return cnt
    else:
        is_even = True if n % 2 == 0 else False
        if is_even:
            cnt += 1
            print(int(n))
            cnt = hailstone(n / 2, cnt)
            return cnt
        else:
            cnt += 1
            print(int(n))
            cnt = hailstone(n * 3 + 1, cnt)
            return cnt


def delete_min_digit(num, min_digit):
    if num == min_digit:
        return 0
    else:
        new_num = 0
        num_list = list()
        while num:
            num_list.insert(0, num % 10)
            num = num // 10
        num_list.remove(min_digit)
        length = len(num_list)
        for i in num_list:
            new_num += i * (10 ** (length - 1))
            length -= 1
        return new_num


def get_min_digit(num):
    min_digit = num % 10
    while num:
        if num % 10 < min_digit:
            min_digit = num % 10
        num = num // 10
    return min_digit


def merge_single(n, merged_num=0, res=0):
    if n == 0:
        return res
    else:
        min_digit = get_min_digit(n)
        res += min_digit * (10 ** merged_num)
        merged_num += 1
        deleted_num = delete_min_digit(n, min_digit)
        res = merge_single(deleted_num, merged_num, res)
        return res


def get_min_digit_both(n1, n2):
    min_digit1 = get_min_digit(n1)
    min_digit2 = get_min_digit(n2)
    if min_digit1 < min_digit2:
        return n1, min_digit1
    else:
        return n2, min_digit2


def merge(n1, n2, merged_num=0, res=0):
    """ Merges two numbers
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    """
    if n1 == 0 or n2 == 0:
        if n1 == 0:
            return res + merge_single(n2) * (10 ** merged_num)
        else:
            return res + merge_single(n1) * (10 ** merged_num)
    else:
        min_digit_num, min_digit = get_min_digit_both(n1, n2)
        if min_digit_num == n1:
            res += min_digit * (10 ** merged_num)
            merged_num += 1
            res = merge(delete_min_digit(min_digit_num, min_digit), n2, merged_num, res)
            return res
        else:
            res += min_digit * (10 ** merged_num)
            merged_num += 1
            res = merge(n1, delete_min_digit(min_digit_num, min_digit), merged_num, res)
            return res


def make_func_repeater(f, x):
    """
    >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
    >>> incr_1(2) #same as f(f(x))
    3
    >>> incr_1(5)
    6
    """
    def repeat(n):
        if n == 0:
            return x
        else:
            return f(repeat(n - 1))
    return repeat


def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    def prime_helper(divisor):
        if n == divisor:
            return True
        elif n % divisor == 0 or n == 1:
            return False
        else:
            return prime_helper(divisor + 1)
    return prime_helper(2)
