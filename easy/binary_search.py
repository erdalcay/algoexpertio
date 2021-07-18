"""
    Binary search.
"""
from typing import List

def binarySearch(nums: List[int], target: int) -> int:
    low, hi = 0, len(nums) - 1
    while low <= hi:
        mid = low + (hi - low) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            hi = mid - 1
        else:
            low = mid + 1
    return -1
