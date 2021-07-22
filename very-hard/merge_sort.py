"""
    Merge sort.
"""
from typing import List


def mergeSort(nums: List[int]) -> List[int]:
    if not nums: 
        return
    
    if len(nums) == 1: 
        return nums

    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]

    return merge(mergeSort(left), mergeSort(right))


def merge(left: List[int], right: List[int]) -> List[int]:
    merged = left + right
    k = l = r = 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            merged[k] = left[l]
            l += 1
        else:
            merged[k] = right[r]
            r += 1
        k += 1
            
    while l < len(left):
        merged[k] = left[l]
        l += 1
        k += 1
        
    while r < len(right):
        merged[k] = right[r]
        r += 1
        k += 1
    
    return merged
