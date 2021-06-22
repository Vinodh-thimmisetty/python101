import unittest

from dsa import btree_traversals
from dsa import utils
from dsa.utils import TreeNode, height_of_tree


class BTreeTraversals(unittest.TestCase):

    def setUp(self) -> None:
        self.input = [1, 2, 3, 4, 5]
        self.root = TreeNode(1)
        self.root.left = TreeNode(2)
        self.root.right = TreeNode(3)
        self.root.left.left = TreeNode(4)
        self.root.left.right = TreeNode(5)

    def test_in_order(self) -> None:
        b_tree = btree_traversals.BinaryTree()
        utils.display_tree(f" Before {b_tree.nodes} ")
        b_tree.left_root_right(self.root)
        utils.display_tree(f" After {b_tree.nodes} ")
        self.assertEqual(b_tree.nodes, [4, 2, 5, 1, 3])

    def test_pre_order(self) -> None:
        b_tree = btree_traversals.BinaryTree()
        utils.display_tree(f" Before {b_tree.nodes} ")
        b_tree.root_left_right(self.root)
        utils.display_tree(f" After {b_tree.nodes} ")
        self.assertEqual(b_tree.nodes, [1, 2, 4, 5, 3])

    def test_post_order(self) -> None:
        b_tree = btree_traversals.BinaryTree()
        utils.display_tree(f" Before {b_tree.nodes} ")
        b_tree.left_right_root(self.root)
        utils.display_tree(f" After {b_tree.nodes} ")
        self.assertEqual(b_tree.nodes, [4, 5, 2, 3, 1])

    def test_height_of_tree(self) -> None:
        self.assertEqual(height_of_tree(self.root), 3)

    def test_breadth_first_recursive(self) -> None:
        b_tree = btree_traversals.BinaryTree()
        utils.display_tree(f" Before {b_tree.nodes} ")
        b_tree.level_order_traversal(self.root)
        utils.display_tree(f" After {b_tree.nodes} ")
        self.assertEqual(b_tree.nodes, [1, 2, 3, 4, 5])

    def test_breadth_first_iterative(self) -> None:
        b_tree = btree_traversals.BinaryTree()
        utils.display_tree(f" Before {b_tree.nodes} ")
        b_tree.level_order_traversal_iterative(self.root)
        utils.display_tree(f" After {b_tree.nodes} ")
        self.assertEqual(b_tree.nodes, [1, 2, 3, 4, 5])

    def tearDown(self) -> None:
        self.input = []
        self.root = None


if __name__ == '__main__':
    unittest.main()
