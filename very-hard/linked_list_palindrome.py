"""
    Given a linked list, check if values of its nodes 
    form a palindrome
"""
from __future__ import annotations


class LinkedList:
    def __init__(self, value: int):
        self.value = value
        self.next = None


def linkedListPalindrome(head: LinkedList) -> bool:
    # Get the number of nodes in the list
    curr, size = head, 0
    while curr:
        size += 1
        curr = curr.next

    # Split the list into two halves, reversing
    # the first half.
    first, second = split_reverse_list(head, size)
    while first:
        if first.value != second.value:
            return False
        first, second = first.next, second.next
    return True


def split_reverse_list(head: LinkedList, size: int) -> Tuple[LinkedList, LinkedList]:
    # Reverse the first half
    curr, prev = head, None
    for _ in range(size // 2):
        curr.next, prev, curr = prev, curr, curr.next

    # Skip the middle node in case of odd list size
    if size % 2:
        second = curr.next
    else:
        second = curr
    return [prev, second]
