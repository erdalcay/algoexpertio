"""
    Given the root node of a graph-like structure,
    implement breadth first search.
"""
from __future__ import annotations


class GraphNode:
    """Graph node instance."""
    def __init__(self, value: int = 0):
        self.value = value
        self.adjacents: List[GraphNode] = []

        
def BFS_graph(node: GraphNode, values: List[int] = None) -> List[int]:
    """Implements breadth first search for a graph structure using a queue."""
    if not node: return
    if not values: values = []
    queue = []
    queue.append(node)
    visited = set()
    while queue:
        curr = queue.pop(0)
        if curr not in visited:
            visited.add(curr)
            values.append(curr.value)
        for adjacent in reversed(curr.adjacents):
            if adjacent not in visited:
                queue.append(adjacent)
    return values


"""
    Given the root node of a tree-like structure,
    implement breadth first search.
"""


class TreeNode:
    """Tree node instance."""
    def __init__(self, value: int = 0, left: TreeNode = None, right: TreeNode = None):
        self.value = value
        self.left = left
        self.right = right

        
def BFS_graph(node: TreeNode) -> List[int]:
    """Implements breadth first search for a tree structure using a queue."""
    if not node: return
    # Stores the values of each node
    values = []
    # Using FIFO to achieve level order traversal.
    queue = []
    queue.append(node)
    visited = set()
    while queue:
        curr = queue.pop(0)
        values.append(curr.value)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return values
