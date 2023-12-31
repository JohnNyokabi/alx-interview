#!/usr/bin/python3
"""function that returns a list of lists of integers
representing the pascals triangle of `n`"""


def pascal_triangle(n):
    """pascal triangle logic"""
    if (n <= 0):
        return []

    tri = [[1]]
    for i in range(1, n):
        curr = [1]
        prev = tri[i - 1]

        for j in range(1, i):
            curr.append(prev[j - 1] + prev[j])

        curr.append(1)
        tri.append(curr)

    return tri
