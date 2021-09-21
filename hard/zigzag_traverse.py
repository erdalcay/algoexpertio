""" 
    Given a 2-d array of integers, 
    return an array of its integers in
    zigzag order.

    Example:

        input: [
            [1, 3, 4],
            [2, 5, 8],
            [6, 7, 9]
        ]

        output : [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
from typing import List


def is_within_bounds(n: int, m: int, i: int, j: int) -> bool:
    if i < 0 or j < 0 or i >= n or j >= m:
        return False
    return True


def zigzagTraverse(M: List[List[int]]) -> List[int]:
    zigzag = []

    if not M:
        return zigzag

    n, m = len(M), len(M[0])
    i, j, go_down = 0, 0, True
    while is_within_bounds(n, m, i, j):
        zigzag.append(M[i][j])
        # Next direction is down
        if go_down:
            # Try to go down & left
            if is_within_bounds(n, m, i + 1, j - 1):
                i += 1
                j -= 1
            # On the last row, can't go deeper down.
            # Go right instead.
            elif i == n - 1:
                go_down = False
                j += 1
            # Go down straight.
            else:
                go_down = False
                i += 1
        # Need to go to up or right
        else:
            # Try to go up & right
            if is_within_bounds(n, m, i - 1, j + 1):
                i -= 1
                j += 1
            # On the last column, can't go up anymore.
            # Go down straight instead.
            elif j == m - 1:
                go_down = True
                i += 1
            # Go right.
            else:
                go_down = True
                j += 1
    return zigzag
