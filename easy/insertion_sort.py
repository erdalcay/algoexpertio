"""
    Insertion sort.
"""
from typing import List


def insertionSort(nums: List[int]) -> List[int]:
    if not nums:
        return []

    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j] < nums[j - 1]:
            swap(nums, j, j - 1)
            j -= 1

    return nums

def swap(nums: List[int], left: int, right: int) -> None:
    nums[left], nums[right] = nums[right], nums[left]
    return None

