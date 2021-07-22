"""
    Bubble sort.
"""
from typing import List


def bubbleSort(nums: List[int]) -> List[int]:
    if not nums:
        return nums

    left, right = 0, 1 
    sort_count = 0
    while sort_count < len(nums) - 1:
        if nums[left] >= nums[right]:
            swap(nums, left, right)
            left += 1
            right += 1
        if right >= len(nums) - sort_count:
            left, right = 0, 1
            sort_count += 1
    return nums

def swap(nums: List[int], left: int, right: int) -> None:
    nums[left], nums[right] = nums[right], nums[left]
    return None

