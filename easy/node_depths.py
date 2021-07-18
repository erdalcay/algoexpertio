"""
    Given a binary tree,
    return the sum of all it's node's
    depths.
"""
from __future__ import annotations

class BinaryTree:
    """Binary tree node instance."""
    def __init__(
        self, 
        value: int = 0,
        left: BinaryTree = None,
        right: BinaryTree = None
    ):
        self.value = value
        self.left = None
        self.right = None

def nodeDepths(root: BinaryTree) -> int:
    return traverse(root)

def traverse(node: BinaryTree, depth = 0) -> int:
    if not node:
        return 0
    return \
        depth \
        + traverse(node.left, depth + 1) \
        + traverse(node.right, depth + 1)
