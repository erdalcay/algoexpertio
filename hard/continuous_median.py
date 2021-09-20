"""
    Calculate the continuous median of a set of numbers
    while new numbers are being added to the set.

    Median should be access in constant time.
"""
from __future__ import annotations
from heapq import heappush, heappop


class ContinuousMedianHandler:
    """
        Gives access to the median in constant time
        as new number being added to the set.

        Idea:
            . Maintain two heaps, one for left and one for right
            side of the middle point.
            . Max heap for left side, min heap for right side.
            . Keep a size difference of maximum 1 item between
            the two heaps.
            . Calculate the heap by peeking both heaps.
    """

    def __init__(self):
        self.left = []  # Max heap
        self.right = []  # Min heap
        self.count = 0
        self.median = None

    def insert(self, number: int) -> None:
        if not self.left or (self.right and number < self.right[0]):
            heappush(self.left, -number)
        else:
            heappush(self.right, number)

        # Keep the size difference at < 2 between left and right split.
        if len(self.left) - len(self.right) == 2:
            heappush(self.right, -heappop(self.left))
        elif len(self.right) - len(self.left) == 2:
            heappush(self.left, -heappop(self.right))

        self.count += 1
        self.median = self.calculate_median()

    def calculate_median(self) -> int:
        if self.count % 2 == 0:
            left, right = -self.left[0], self.right[0]
            return (left + right) / 2
        if len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return self.right[0]

    def get_median(self) -> int:
        return self.median
