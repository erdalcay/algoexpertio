"""
    Given a singly linked list,
    create a zip of the list.

    A linked list is zipped if its nodes
    are in the following order:

    `1st node -> kth node -> 2nd node -> (k-1)th node`

    where k is the length of the list.
"""
from __future__ import annotations


class LinkedList:
    def __init__(self, value: int):
        self.value = value
        self.next = None


def zipLinkedList(head: LinkedList) -> LinkedList:
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    prev = None
    while slow:
        slow.next, prev, slow = prev, slow, slow.next

    odd_turn = True
    first, second = head, prev
    while first.next:
        if odd_turn:
            first.next, first = second, first.next
            odd_turn = False
        else:
            second.next, second = first, second.next
            odd_turn = True

    return head
