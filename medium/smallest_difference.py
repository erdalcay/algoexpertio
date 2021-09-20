"""
    Given two arrays of integers, find a pair (one from each array)
    that has the smallest difference.
"""
from typing import List


def smallestDifference(A: List[int], B: List[int]) -> List[int]:
    if not A or not B:
        return [-1, -1]

    A.sort()
    B.sort()

    diff = float("inf")
    selected = [-1, -1]

    i, j = 0, 0
    while i < len(A) and j < len(B):
        a, b = A[i], B[j]
        if a == b:
            return [a, b]

        if a < b:
            i += 1
        else:
            j += 1

        d = abs(a - b)
        if d < diff:
            diff, selected = d, [a, b]

    return selected
