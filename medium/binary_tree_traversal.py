"""
    Given the root of a binary search tree,
    implement three traversal functions:	
        - Pre-order
        - In-order
        - Post-order

    Each function should return the values of 
    each node in the order of traversal.
"""
from __future__ import annotations


class BSTNode:
    "Binary search tree node instance."
    def __init__(self, value: int = 0, left: BSTNode = None, right: BSTNode = None):
        self.value = value
        self.left = left
        self.right = right

        
def preOrderTraverse(node: BSTNode, values: List[int] = []) -> List[int]:
    """Root > Left > Right"""
    if not node: return
    values.append(node.value)
    preOrderTraverse(node.left, values)
    preOrderTraverse(node.right, values)
    return values
        
    
def inOrderTraverse(node: BSTNode, values: List[int] = []) -> List[int]:
    """Left > Root > Right"""
    if not node: return
    inOrderTraverse(node.left, values)
    values.append(node.value)
    inOrderTraverse(node.right, values)
    return values


def postOrderTraverse(node: BSTNode, values: List[int] = []) -> List[int]:
    """Left > Right > Root"""
    if not node: return
    postOrderTraverse(node.left, values)
    postOrderTraverse(node.right, values)
    values.append(node.value)
    return values
