"""
    Given a a list of intervals, merge any
    overlapping interval and return the result
    in no particular order.
"""
from typing import List


def mergeOverlappingIntervals(I: List[List[int]]) -> List[List[int]]:
    I.sort(key=lambda x: x[0])

    merged = []
    for i in range(len(I) - 1):
        curr, next = I[i][1], I[i + 1][0]

        if curr >= next:
            start, end = I[i][0], I[i + 1][1]
            I[i + 1] = [start, max(curr, end)]
        else:
            merged.append(I[i])

    merged.append(I[-1])
    return merged
