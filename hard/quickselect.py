"""
    Given an array of integers, return the kth smallest item
    using quickselect.
"""
from typing import List


def swap(nums: List[int], i: int, j: int) -> None:
    nums[i], nums[j] = nums[j], nums[i]
    return


def quickselect(nums: List[int], k: int) -> int:
    start, end = 0, len(nums) - 1
    while True:
        pivot, left, right = start, start + 1, end
        while left <= right:
            if nums[left] > nums[pivot] and nums[right] < nums[pivot]:
                swap(nums, left, right)
            if nums[left] <= nums[pivot]:
                left += 1
            if nums[right] >= nums[pivot]:
                right -= 1
        swap(nums, pivot, right)
        if right == k - 1:
            return nums[right]
        if right < k - 1:
            start = right + 1
        else:
            end = right - 1
    return -1
