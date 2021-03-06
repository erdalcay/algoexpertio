"""
    Given the root of a binary tree,
    invert the tree.

    Of course..
"""
from __future__ import annotations


class BinaryTreeNode:
    """Binary tree node instance."""
    def __init__(self, data: int = 0, left: BinaryTreeNode = None, right: BinaryTreeNode = None):
        self.data = data
        self.left = left
        self.right = right


def invertBinaryTree(node: BinaryTreeNode) -> None:
    """Inverts a binary tree."""
    if not node: return

    # Swap left and right children, 
    # repeat for each node.
    node.left, node.right = node.right, node.left
    invertBinaryTree(node.left)
    invertBinaryTree(node.right)
