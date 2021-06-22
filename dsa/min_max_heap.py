"""
    Complete Binary Tree ( All Levels are filled with LEFT Child preference)
    Level Order Traversal ( Parent Node have min/max compared to both left & right child nodes of Tree)
    Algorithms:
        Insert: Bottom-Up Approach
            1) Insert @Last Level
            2) Compare with Parent & Swap
            No.of Operations = No.of Levels in a Tree ==> O(lg n)
        Delete: Top-Down Approach
            1) move Last Node Value to Root
            2) Compare the Root with its childrens
            No.of Operations = No.of Levels in a Tree ==> O(lg n)
        IS_Heap: Top-Down Approach
            1) For every Parent Node, check whether Left/Right nodes are lesser
            2) Loop till Last Level
            3) Level Order ( Queue implementation) might be good.

"""


class MinHeap:

    def __init__(self):
        self.heap = []

    def create_heap(self, items):
        self.heap = list(items)

    def heap_size(self):
        return len(self.heap)

    def heapify(self, items):
        for item in items:
            self.push(item)

    def is_heap(self):
        if self.heap_size() == 0:
            raise ValueError("Heap is Empty !!")
        if self.heap_size() == 1:
            return True
        parent_idx = 0
        while parent_idx < self.heap_size():
            if self.has_left_child(parent_idx):
                if self.has_right_child(parent_idx):
                    if self.heap[self.left_child_idx(parent_idx)] < self.heap[parent_idx] or \
                            self.heap[self.right_child_idx(parent_idx)] < self.heap[parent_idx]:
                        return False
                else:
                    if self.heap[self.left_child_idx(parent_idx)] < self.heap[parent_idx]:
                        return False
            parent_idx = parent_idx + 1
        return True

    def parent_idx(self, child_idx):
        return (child_idx - 1) // 2

    def left_child_idx(self, parent_idx):
        return 2 * parent_idx + 1

    def right_child_idx(self, parent_idx):
        return 2 * parent_idx + 2

    def has_parent(self, child_idx):
        return self.parent_idx(child_idx) >= 0

    def has_left_child(self, parent_idx):
        return self.left_child_idx(parent_idx) < len(self.heap)

    def has_right_child(self, parent_idx):
        return self.right_child_idx(parent_idx) < len(self.heap)

    def swap_parent_child(self, parent_idx, child_idx):
        self.heap[parent_idx], self.heap[child_idx] = self.heap[child_idx], self.heap[parent_idx]

    def peek(self):
        if len(self.heap) > 0:
            return self.heap[0]
        else:
            raise ValueError("Heap is Empty")

    def push(self, item):
        self.heap.append(item)
        self.bubble_up()

    def poll(self):
        heap_size = len(self.heap)
        if heap_size > 0:
            self.heap[0] = self.heap[heap_size - 1]
            del self.heap[heap_size - 1]  # This is important....
            self.bubble_down()
        else:
            raise ValueError("Heap is Empty")

    def bubble_up(self):
        heap_size = len(self.heap)
        if heap_size > 1:
            current_idx = heap_size - 1
            while self.has_parent(current_idx) and self.heap[current_idx] < self.heap[self.parent_idx(current_idx)]:
                parent_idx = self.parent_idx(current_idx)
                self.swap_parent_child(parent_idx, current_idx)
                current_idx = parent_idx

    def bubble_down(self):
        parent_idx = 0
        while self.has_left_child(parent_idx):
            """
                1. Compare the Children to identify Min
                2. Compare the Min Child Node with Parent
                3. Swap only if Child Node has LESSER Value to parent Node
            """
            if self.has_right_child(parent_idx) and \
                    self.heap[self.left_child_idx(parent_idx)] > self.heap[self.right_child_idx(parent_idx)]:
                smallest = self.right_child_idx(parent_idx)
            else:
                smallest = self.left_child_idx(parent_idx)

            if self.heap[smallest] < self.heap[parent_idx]:
                self.swap_parent_child(smallest, parent_idx)
                parent_idx = smallest
            else:
                break

    def display_tree(self):
        print("*" * (len(self.heap) * 5))
        print(self.heap)
        print("*" * (len(self.heap) * 5))
