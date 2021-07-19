"""
    Given a string, return the first 
    non-repeating character's index.
"""
from collections import defaultdict


def firstNonRepeatingCharacter(string: str) -> int:
    chars = defaultdict(int)
    for char in string:
        chars[char] += 1
    for i, char in enumerate(string):
        if chars[char] == 1:
            return i
    return -1
