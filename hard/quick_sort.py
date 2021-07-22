"""
    Quick sort.
"""
from typing import List


def quickSort(nums: List[int]) -> List[int]:
	quickSortRecursion(nums, 0, len(nums) - 1)
    return nums


def quickSortRecursion(nums: List[int], start: int, end: int) -> None:
	if start - end >= 0:
		return
	# Select pivot and left & right pointers
	pivot, left, right = start, start + 1, end
	while right >= left:
		# 1. 
		if nums[left] > nums[pivot] and nums[right] < nums[pivot]:
			swap(nums, left, right)
		# 2. if left is smaller than or equal to the pivot, move left
		if nums[left] <= nums[pivot]:
			left += 1
		# 3. if right is greater than or equal to the pivot, move right
		if nums[right] >= nums[pivot]:
			right -= 1
	swap(nums, pivot, right)
	# Choose the smaller sub array.
	is_left_smaller = right - start < end - right                                                                                                                                                                                        
	# Call the recursion on the smaller one first
	if is_left_smaller:
		quickSortRecursion(nums, start, right - 1)
		quickSortRecursion(nums, right + 1, end)
	else:
		quickSortRecursion(nums, right + 1, end)
		quickSortRecursion(nums, start, right - 1)
	return None


def swap(nums: List[int], left: int, right: int) -> None:
	nums[left], nums[right] = nums[right], nums[left]
	return None
