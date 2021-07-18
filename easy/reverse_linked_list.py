"""
    Given the head of a linked list,
    reverse the list. 

    Of course...
"""

from __future__ import annotations

class ListNode:
    """List node instance."""
    def __init__(self, data: int = 0, next: ListNode = None):
        self.data = data
        self.next = next


def reverseLinkedList(head: ListNode) -> ListNode:
    """Reverses the linked list, returns the new head."""
    curr, prev = head, None

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev
