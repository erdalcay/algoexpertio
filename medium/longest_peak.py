"""
Given an array of integers, 
return the length of the longest 
peak sequence.

A peak is a list of adjacent integers 
that are strictly increasing until 
they reach a tip at which point 
they become strictly decreasing.

To form a peak, at least 3 integers
are needed.
"""

def longestPeak(array):
    # Base case
    if len(array) < 3:
        return 0

    peak, i = 0, 1
    while i < len(array) - 1:
        # Left, middle and right pointers
        l, m, r = i - 1, i, i + 1
        # The triplet doesn't form a peak,
        # slide the window to the right by one.
        if not array[l] < array[m] > array[r]:
            i += 1
            continue
        # We found a peak, 
        # Now we need to search in both
        # directions to see if adjacent elements
        # can be included in the peak.
        curr_peak = 3

        # Move left
        l -= 1
        while l >= 0 and array[l] < array[l + 1]:
            curr_peak += 1
            l -= 1

        # Move right
        r += 1
        while r < len(array) and array[r] < array[r - 1]:
            curr_peak += 1
            r += 1

        peak = max(curr_peak, peak)
        # Below is how we achieve linear time complexity.
        # We can't have two peaks (l-m-r) in the given range
        # That is why we are moving the window to the
        # furthest possible point (from left to right).
        i = r

return peak
