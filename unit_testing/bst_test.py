import unittest

from dsa.bst import BinarySearchTree
from dsa.utils import TreeNode


class BalancedBinarySearchTreeTests(unittest.TestCase):

    def setUp(self) -> None:
        self.input = [1, 2, 3, 4, 5]
        self.root: TreeNode = TreeNode(8)
        self.root.left = TreeNode(3)
        self.root.right = TreeNode(10)
        self.root.left.left = TreeNode(1)
        self.root.left.right = TreeNode(6)
        self.root.right.right = TreeNode(14)
        self.root.left.right.left = TreeNode(4)
        self.root.left.right.right = TreeNode(7)

    def test_bst_search(self):
        bst = BinarySearchTree()

        self.assertTrue(bst.search(self.root, 4))
        bst.delete(self.root, 4)
        self.assertFalse(bst.search(self.root, 4))
        bst.insert(self.root, 4)

        self.assertTrue(bst.search(self.root, 10))
        bst.delete(self.root, 10)
        self.assertFalse(bst.search(self.root, 10))
        bst.insert(self.root, 10)

        self.assertTrue(bst.search(self.root, 3))
        bst.delete(self.root, 3)
        self.assertFalse(bst.search(self.root, 3))
        bst.insert(self.root, 3)

    @unittest.skip("TODO")
    def test_red_black_tree(self):
        pass  # Yet To Implement

    @unittest.skip("TODO")
    def test_avl_tree(self):
        pass  # Yet To Implement

    def tearDown(self) -> None:
        self.input = []


if __name__ == '__main__':
    unittest.main()
