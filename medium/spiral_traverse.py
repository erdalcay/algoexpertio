"""
    Given a 2-d array of numbers, 
    flatten it using a spiral shape traversal.
"""
from __future__ import annotations


def get_directions(i: int, j: int) -> List[int]:
    return [
        [i, j + 1],  # Right
        [i + 1, j],  # Down
        [i, j - 1],  # Left
        [i - 1, j],  # Up
    ]


def find_next_direction(n: int, m: int, directions: List[int], dp: List[List[int]]) -> Tuple[int, int, int]:
    for idx, (i, j) in enumerate(directions):
        if not is_out_of_bounds(n, m, i, j) and not dp[i][j]:
            return (i, j, idx)
    return (-1, -1, -1)


def is_out_of_bounds(n: int, m: int, i: int, j: int) -> bool:
    if i < 0 or j < 0 or i >= n or j >= m:
        return True
    return False


def spiralTraverse(matrix: List[int]) -> List[int]:
    spiral = []

    if not matrix:
        return spiral

    n, m = len(matrix), len(matrix[0])
    dp = [[False] * m for _ in range(n)]

    i, j, curr = 0, 0, 0
    while i < n and j < m and len(spiral) < n * m:
        row, col = matrix[i], matrix[i][j]
        spiral.append(col)
        dp[i][j] = True

        # Determine next move direction.

        # Check current direction first as the idea is
        # to move in the same direction until can not.
        directions = get_directions(i, j)
        a, b = directions[curr]
        if not is_out_of_bounds(n, m, a, b) and not dp[a][b]:
            i, j = a, b
        # Try other directions.
        else:
            i, j, curr = find_next_direction(n, m, directions, dp)

    return spiral
