from typing import List


class TreeNode:
    def __init__(self, value):
        self._value = value
        self.left = self.right = None

    @property
    def value(self):
        return self._value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left):
        self._left = left

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right):
        self._right = right


def display_tree(nodes: List):
    print("*" * (len(nodes)))
    print(nodes)
    print("*" * (len(nodes)))


def height_of_tree(root: TreeNode):
    if not root:
        return 0
    left_tree_height = height_of_tree(root.left)
    right_tree_height = height_of_tree(root.right)
    return 1 + max(left_tree_height, right_tree_height)
