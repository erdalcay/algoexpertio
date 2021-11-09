"""
    Given a `nxm` grid of 0s and 1s, remove islands.

    An island is a set of `1s` that are not vertically or 
    horizontally connected to another set of `1s` that are not
    touching the borders of the grid/matrix.

    Removing means inverting the value of island nodes. (`1` ==> `0`)

    Example:

    Matrix:
    [   
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1]
    ]

    Islands:
    [   
        [-, -, -, -, -, -],
        [-, 1, -, -, -, -],
        [-, -, 1, -, -, -],
        [-, -, -, -, -, -],
        [-, -, 1, 1, -, -],
        [-, -, -, -, -, -]
    ]

    Removed:
    [   
        [1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1]
    ]
"""
from typing import List, Tuple


def get_neighbors(i: int, j: int) -> List[Tuple[int]]:
    """Returns all possible horizontal/vertical movement within the grid."""
    return [
        (i + 1, j),
        (i - 1, j),
        (i, j + 1),
        (i, j - 1),
    ]


def is_out_of_bounds(n: int, m: int, i: int, j: int) -> bool:
    """Checks whether `i and j` is a valid index."""
    if i < 0 or j < 0 or i >= n or j >= m:
        return True
    return False


def is_border(n: int, m: int, i: int, j: int) -> bool:
    """Checks whether `i and j` is on one of the edges of the grid."""
    if i == 0 or j == 0 or i == n - 1 or j == m - 1:
        return True
    return False


def DFS(
    M: List[List[int]], dp: List[List[bool]], n: int, m: int, i: int, j: int
) -> None:
    """Explores all nearby `1s` starting from `i` and `j`."""
    if is_out_of_bounds(n, m, i, j) or dp[i][j] or M[i][j] == 0:
        return None

    dp[i][j] = True

    neighbors = get_neighbors(i, j)
    for row, col in neighbors:
        DFS(M, dp, n, m, row, col)
    return None


def remove_islands(M: List[List[int]]) -> List[List[int]]:
    # Get the size of the grid
    n, m = len(M), len(M[0])
    # Maintaining a `visited` list to keep track of unexplored nodes.
    dp = [[False] * m for _ in range(n)]

    # Iterate through all nodes and start exploring nearby `1s`
    # whenever we come accross a `1` that is also a border in the matrix.
    # The result of this operation is `dp` having all `1s` that are
    # connected to a border (by either horizontal or vertical adjacency) marked
    # as `True`.
    for i, row in enumerate(M):
        for j, col in enumerate(row):
            if col == 1 and not dp[i][j] and is_border(n, m, i, j):
                DFS(M, dp, n, m, i, j)

    # At this point any unvisited nodes with a value of `1` is part of an island,
    # and we can invert their values.
    for i, row in enumerate(M):
        for j, col in enumerate(row):
            if not dp[i][j] and col == 1:
                M[i][j] = 0

    return M
