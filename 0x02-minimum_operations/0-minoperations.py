#!/usr/bin/python3
"""
Method that calculates the fewest number of operations
needed to result in exactly n H characters in the file
"""


def counter(num):
    """counts list of operations"""
    c = 1
    list_op = []
    i = num

    while i != 1:
        c += 1
        if i % c == 0:
            while (i % c == 0 and i != 1):
                i /= c
                list_op.append(c)

    return list_op


def minOperations(n) -> int:
    """Returns total number of operations until nH"""
    if (type(n) is not int) or (n < 2):
        return 0
    res = counter(n)
    return sum(res)
