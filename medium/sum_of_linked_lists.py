"""
    Given two linked lists, sum the values
    of nodes that are in the same position
    in both lists.
"""
from __future__ import annotations


class LinkedList:
    """Linked list node constructor."""
    
    def __init__(self, value: int = 0, next: LinkedList = None):
        self.value = value
        self.next = next

        
def sumOfLinkedLists(l1: LinkedList, l2: LinkedList) -> LinkedList:
    curr = dummy = LinkedList()
    carry = 0
    while l1 and l2:
        total = l1.value + l2.value + carry
        carry = 1 if total >= 10 else 0
        total = total % 10 if total >= 10 else total
        curr.next = curr = LinkedList(total)
        l1, l2 = l1.next, l2.next

    while l1:
        total = l1.value + carry
        carry = 1 if total >= 10 else 0
        total = total % 10 if total >= 10 else total
        curr.next = curr = LinkedList(total)
        l1 = l1.next

    while l2:
        total = l2.value + carry
        carry = 1 if total >= 10 else 0
        total = total % 10 if total >= 10 else total
        curr.next = curr = LinkedList(total)
        l2 = l2.next

    if carry:
        curr.next = LinkedList(carry)

    return dummy.next
