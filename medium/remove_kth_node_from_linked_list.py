"""
    Given the head of a linked list and an integer k, 
    remove the kth node from the end of the list.

    Must be in-place and nodes need to be mutated in 
    case of position shifts.
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class LinkedList:
    value: int = 0
    next: LinkedList = None


def removeKthNodeFromEnd(head: LinkedList, k: int) -> None:
    if not head:
        return

    # Find the size of the list
    curr, size = head, 0
    while curr:
        size += 1
        curr = curr.next

    # Get the actual k in case of k > list size
    k %= size

    # Special case for the head node as the question
    # requires mutation to shift the nodes.
    if k == 0:
        while head and head.next:
            next = head.next
            head.value = head.next.value
            head.next = next.next
            head = next
            head.next = None
        return

    # Find the kth node
    curr, prev, i = head, None, 0
    while (size - i) > k:
        prev = curr
        curr = curr.next
        i += 1

    # If kth node is not the last node
    if curr:
        prev.next = curr.next
        curr.next = None
    # If last node
    else:
        prev.next = None
    return
