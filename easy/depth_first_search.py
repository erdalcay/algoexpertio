"""
    Given the root node of a graph-like structure,
    implement depth first search.
"""
from __future__ import annotations


class GraphNode:
    """Graph node instance."""
    def __init__(self, value: int = 0):
        self.value = value
        self.adjacents: List[GraphNode] = []

        
def DFS_iterative(node: GraphNode) -> None:
    """Implements depth first search for a graph structure using a stack."""
    if not node:
        return
    stack = []
    stack.append(node)
    visited = set()
    while stack:
        curr = stack.pop()
        if curr not in visited:
            visited.add(curr)
        for adjacent in reversed(curr.adjacents):
            if adjacent not in visited:
                stack.append(adjacent)
    return None


def DFS_recursive(node: GraphNode, values: List[int] = None, visited: Set[GraphNode] = None) -> List[int]:
    """Recursive implementation for graph dfs."""
    if not node: return
    if not values: values = []
    if not visited: visited = set()
    if node in visited: return
    visited.add(node)
    values.append(node.value)
    for adjacent in node.adjacents:
        DFS_recursive(adjacent, values, visited)
    return values

