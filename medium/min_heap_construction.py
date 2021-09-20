from typing import List


class MinHeap:
    def __init__(self, array: List[int]):
        self.heap = self.buildHeap(array)

    def buildHeap(self, array: List[int]) -> List[int]:
        """
            Heapifies a list of numbers in place and returns it.

            Steps:
                1) Find the last parent item in the given list.
                2) Sift every parent down starting from the last one.
        """
        last_parent_idx = (len(array) - 2) // 2
        for parent_idx in reversed(range(last_parent_idx + 1)):
            self.siftDown(array, parent_idx)
        return array

    def siftDown(self, array: List[int], curr_idx: int) -> None:
        """
            Moves an item down until it is in the correct position.

            Steps:
                1) Find the left & right child of the current item.
                2) Select the one with the lower value.
                3) Swap the selected child with the current item.
                4) Go until the end of the heap.
        """
        left_child_idx = 2 * curr_idx + 1
        while left_child_idx < len(array):
            right_child_idx = 2 * curr_idx + 2
            if right_child_idx < len(array) and array[right_child_idx] < array[left_child_idx]:
                idx_to_swap = right_child_idx
            else:
                idx_to_swap = left_child_idx

            if array[idx_to_swap] >= array[curr_idx]:
                return
            self.swap(array, idx_to_swap, curr_idx)
            curr_idx = idx_to_swap
            left_child_idx = 2 * curr_idx + 1
        return

    def siftUp(self, curr_idx: int) -> None:
        """
            Moves an item up until it is in the correct position.

            Steps:
                1) Find the parent of the item. ((i - 1) / 2)
                2) If parent has a larger value, swap them.
                3) Continue until the peek of the heap.
        """
        parent_idx = (curr_idx - 1) // 2
        while parent_idx > 0 and self.heap[curr_idx] < self.heap[parent_idx]:
            self.swap(self.heap, parent_idx, curr_idx)
            curr_idx = parent_idx
            parent_idx = (curr_idx - 1) // 2
        return

    def peek(self):
        """Returns the item at the top of the heap."""
        if not len(self):
            return None
        return self.heap[0]

    def remove(self):
        """
            Removes the item at the top of the heap and returns it.

            Steps:
                1) Swap the first item with the last one.
                2) Pop the last item.
                3) Sift the first item down until it is in the correct 
                position.
        """
        self.swap(self.heap, 0, len(self.heap) - 1)
        peek = self.heap.pop()
        self.siftDown(self.heap, 0)
        return peek

    def insert(self, value: int) -> None:
        """
            Inserts a new item to the heap.

            Steps:
                1) Send the item to the end of the heap.
                2) Sift it up until it is placed correctly.
        """
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1)
        return

    def swap(self, array: List[int], i: int, j: int) -> None:
        array[i], array[j] = array[j], array[i]
        return

    def __len__(self) -> int:
        return len(self.heap)
