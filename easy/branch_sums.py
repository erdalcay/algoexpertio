"""
    Given the root node of a binary tree,
    return the list of its branch sums, ordered
    from leftmost branch to the rightmost one.
"""
from __future__ import annotations
from typing import List, Tuple


class BinaryTree:
    """Binary tree node instance."""

    def __init__(self, value: int = 0, left: BinaryTree = None, right: BinaryTree = None):
    self.value = value
    self.left = None
    self.right = None


def branchSums_iterative(root: BinaryTree) -> List[int]:
    if not root:
        return []
    sums: List[int] = []
    stack: List[Tuple[int, BinaryTree]] = []
    stack.append((root.value, root))
    while stack:
        value, node = stack.pop()
        if not node.left and not node.right:
            sums.append(value)
        if node.right:
            stack.append((value + node.right.value, node.right))
        if node.left:
            stack.append((value + node.left.value, node.left))
    return sums


def branchSums_recursive(root: BinaryTree, carry: int = 0, sums: List[int] = None) -> List[int]:
    if not root:
        return
    if sums is None:
        sums = []
    carry += root.value
    if not root.left and not root.right:
        sums.append(carry)
    branchSums_recursive(root.left, carry, sums)
    branchSums_recursive(root.right, carry, sums)
    return sums
