from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Node:
    key: int
    value: int
    next: Node = None
    prev: Node = None


class LinkedList:

    _sentinel: Node
    _size: int

    def __init__(self):
        self._sentinel = Node(0, 0)
        self._sentinel.next = self._sentinel
        self._sentinel.prev = self._sentinel
        self._size = 0

    def insert(self, node: Node) -> None:
        """Inserts a new node to the head of the list."""
        node.next = self._sentinel.next
        node.prev = self._sentinel
        node.next.prev = node
        node.prev.next = node
        self._size += 1
        return

    def pop(self) -> Node:
        """Removes and returns the tail of the list."""
        if not len(self):
            return None
        tail = self._sentinel.prev
        tail.next.prev = tail.prev
        tail.prev.next = tail.next
        self._size -= 1
        return tail

    def use(self, node: Node) -> None:
        """Moves the given node to the head of the list."""
        node.next.prev = node.prev
        node.prev.next = node.next
        node.next = self._sentinel.next
        node.prev = self._sentinel
        node.next.prev = node
        node.prev.next = node
        return

    def head(self) -> Node:
        if not len(self):
            return None
        return self._sentinel.next

    def __len__(self) -> int:
        return self._size


class LRUCache:

    capacity: int
    cache: LinkedList
    keys: Dict[str, Node]

    def __init__(self, capacity: int = 1):
        self.capacity = capacity
        self.cache = LinkedList()
        self.keys = {}

    def insertKeyValuePair(self, key: str, value: int) -> None:
        if key in self.keys:
            node = self.keys[key]
            node.value = value
            self.cache.use(node)
        else:
            if len(self.cache) == self.capacity:
                lru = self.cache.pop()
                del self.keys[lru.key]
            node = Node(key, value)
            self.keys[key] = node
            self.cache.insert(node)

    def getValueFromKey(self, key: str) -> int:
        if key not in self.keys:
            return None
        node = self.keys[key]
        self.cache.use(node)
        return node.value

    def getMostRecentKey(self) -> str:
        mru = self.cache.head()
        if not mru:
            return None
        return mru.key
