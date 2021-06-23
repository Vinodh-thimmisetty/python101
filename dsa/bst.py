"""
    Self-Balanced Binary Search Tree
    Avoid Skewness
"""
from dsa.utils import TreeNode


class BinarySearchTree:

    def search(self, root: TreeNode, item: int):
        """
                      8
                   /    \
                  3      10
                /  \    /  \
              1     6  X    14
            /  \  /  \     /  \
           X   X 4    7   X    X
                /  \ / \
               X    X   X

        E.g: Search For (4)

        Step0: Empty Stack
                       ---------------------------------
             STACK:    |   |   |   |   |   |   |   |  |
                       ---------------------------------

        Step1: [ 4 < 8 ] -> So, Search Left
                       ---------------------------------
             STACK:    |   |   |   |   |   |   |   | 8 |
                       ---------------------------------

        Step2: [ 4 > 3 ] -> So, Search Right
                       ---------------------------------
             STACK:    |   |   |   |   |   |   | 3 | 8 |
                       ---------------------------------

        Step3: [ 4 < 6 ] -> So, Search Left
                       ---------------------------------
             STACK:    |   |   |   |   |   | 6 | 3 | 8 |
                       ---------------------------------

        Step4: [ 4 == 4 ] -> Match Found
                       ---------------------------------
             STACK:    |   |   |   |   | 4 | 6 | 3 | 8 |
                       ---------------------------------

        Step5:  returns TRUE
                       ---------------------------------
             STACK:    |   |   |   |   |   | 6 | 3 | 8 |
                       ---------------------------------

        Step6:  returns TRUE
                       ---------------------------------
             STACK:    |   |   |   |   |   |   | 3 | 8 |
                       ---------------------------------

        Step7:  returns TRUE
                       ---------------------------------
             STACK:    |   |   |   |   |   |   |   | 8 |
                       ---------------------------------

        Step8:  returns TRUE
                       ---------------------------------
             STACK:    |   |   |   |   |   |   |   |   |
                       ---------------------------------

        :param root:
        :param item:
        :return:
        """
        if not root:
            return False
        if root.value == item:
            return True
        if item < root.value:
            return self.search(root.left, item)
        else:
            return self.search(root.right, item)

    def insert(self, root: TreeNode, item: int):
        """
                      8
                   /    \
                  3      10
                /  \    /  \
              1     6  X    14
            /  \  /  \     /  \
           X   X 4    7   X    X
                /  \ / \
               X    X   X

        E.g: Insert (5) --> Find the position like Search

        Step0: Empty Stack
                       ---------------------------------
             STACK:    |   |   |   |   |   |   |   |  |
                       ---------------------------------

        Step1: [ 5 < 8 ] -> So, Search Left :: { root: 8, left: 3, right: 10}
                       ---------------------------------
             STACK:    |   |   |   |   |   |   |   | 8 |
                       ---------------------------------

        Step2: [ 5 > 3 ] -> So, Search Right :: { root:3, left: 1, right: 6}
                       ---------------------------------
             STACK:    |   |   |   |   |   |   | 3 | 8 |
                       ---------------------------------

        Step3: [ 5 < 6 ] -> So, Search Left :: { root:6, left: 4, right: 7}
                       ---------------------------------
             STACK:    |   |   |   |   |   | 6 | 3 | 8 |
                       ---------------------------------

        Step4: [ 5 > 4 ] -> So, Search Right :: { root:4, left: Nil, right: Nil}
                       ---------------------------------
             STACK:    |   |   |   |   | 4 | 6 | 3 | 8 |
                       ---------------------------------

        Step5: Right is Nil. So, Create Node with 5 to RIGHT of 4
                       ---------------------------------
             STACK:    |   |   |   | 5 | 4 | 6 | 3 | 8 |
                       ---------------------------------

        Step6: return {root: 4, left: Nil, right: 5}
                       ---------------------------------
             STACK:    |   |   |   |   |   | 6 | 3 | 8 |
                       ---------------------------------

        Step7: return { root:6, left: 4, right: 7}
                       ---------------------------------
             STACK:    |   |   |   |   |  |  | 3 | 8 |
                       ---------------------------------

        Step8: return { root:3, left: 1, right: 6}
                       ---------------------------------
             STACK:    |   |   |  |   |   |   |   | 8 |
                       ---------------------------------

        Step9: return { root:8, left: 3, right: 10}
                       ---------------------------------
             STACK:    |   |   |  |   |   |   |   |   |
                       ---------------------------------


        :param root:
        :param item:
        :return:
        """
        if not root:
            return TreeNode(item)
        if item < root.value:
            root.left = self.insert(root.left, item)
        else:
            root.right = self.insert(root.right, item)
        return root

    def delete(self, root: TreeNode, item):
        """
        CASE-1: If Node is Leaf(4), set it's parent(6)'s left to Nil

                      8
                   /    \
                  3      10
                /  \    /  \
              1     6  X    14
            /  \  /  \     /  \
           X   X 4    7   X    X
                /  \ / \
               X    X   X

        Step0: Empty Stack
                       ---------------------------------
             STACK:    |   |   |   |   |   |   |   |  |
                       ---------------------------------

        Step1: [ 4 < 8 ] -> So, Search Left :: { root: 8, left: 3, right: 10}
                       ---------------------------------
             STACK:    |   |   |   |   |   |   |   | 8 |
                       ---------------------------------

        Step2: [ 4 > 3 ] -> So, Search Right :: { root:3, left: 1, right: 6}
                       ---------------------------------
             STACK:    |   |   |   |   |   |   | 3 | 8 |
                       ---------------------------------

        Step3: [ 4 < 6 ] -> So, Search Left :: { root:6, left: 4, right: 7}
                       ---------------------------------
             STACK:    |   |   |   |   |   | 6 | 3 | 8 |
                       ---------------------------------

        Step4: [ 4 == 4 ] -> Match Found { root:4, left: Nil, right: Nil}
                       ---------------------------------
             STACK:    |   |   |   |   | 4 | 6 | 3 | 8 |
                       ---------------------------------

        Step5: Both LEFT & RIGHT are Nil, so -> return None (which is LEFT of 6)
                       ---------------------------------
             STACK:    |   |   |   |   |  | 6 | 3 | 8 |
                       ---------------------------------

        Step6: return { root:6, left: None, right: 7}
                       ---------------------------------
             STACK:    |   |   |   |   |  |  | 3 | 8 |
                       ---------------------------------

        Step7: return { root:3, left: 1, right: 6}
                       ---------------------------------
             STACK:    |   |   |  |   |   |   |   | 8 |
                       ---------------------------------

        Step8: return { root:8, left: 3, right: 10}
                       ---------------------------------
             STACK:    |   |   |  |   |   |   |   |   |
                       ---------------------------------

        CASE-2: If Node(10) has Only ONE Child(14), Swap Leaf(14) with its parent(10) and remove new Leaf(10) node.
                      8
                   /    \
                  3      10
                /  \    /  \
              1     6  X    14
            /  \  /  \     /  \
           X   X 4    7   X    X
                /  \ / \
               X    X   X


        Step0: Empty Stack
                       ---------------------------------
             STACK:    |   |   |   |   |   |   |   |  |
                       ---------------------------------

        Step1: [ 10 > 8 ] -> So, Search Right :: { root: 8, left: 3, right: 10}
                       ---------------------------------
             STACK:    |   |   |   |   |   |   |   | 8 |
                       ---------------------------------

        Step2: [ 10 == 10 ] -> Match Found :: {root: 10, left: Nil, right: 14}
                       ---------------------------------
             STACK:    |   |   |   |   |   |   | 10 | 8 |
                       ---------------------------------

        Step3: [ 10 has only Right Child { root:14, left: Nil, right: Nil} , so swap it]
                       ---------------------------------
             STACK:    |   |   |   |   |   |  |  | 8 |
                       ---------------------------------

        Step4: return { root:8, left: 3, right: 14}
                       ---------------------------------
             STACK:    |   |   |  |   |   |   |   |   |
                       ---------------------------------


        CASE-3: If Node(3) has both Children (1) & (6):
                        a)  Find Next Inorder Successor(4) (next min val in RIGHT subtree from that Node.)
                        b) Swap and Remove Inorder successor Node

                      8
                   /    \
                  3      10
                /  \    /  \
              1     6  X    14
            /  \  /  \     /  \
           X   X 4    7   X    X
                /  \ / \
               X    X   X

        Step0: Empty Stack
                       ---------------------------------
             STACK:    |   |   |   |   |   |   |   |  |
                       ---------------------------------

        Step1: [ 3 < 8 ] -> So, Search Left :: { root: 8, left: 3, right: 10}
                       ---------------------------------
             STACK:    |   |   |   |   |   |   |   | 8 |
                       ---------------------------------

        Step2: [ 3 == 3 ] -> Match Found :: {root: 3, left: 1, right: 6}
                       ---------------------------------
             STACK:    |   |   |   |   |   |   | 3 | 8 |
                       ---------------------------------

        Step3: Node 3 has both Left({ root:1, left: Nil, right: Nil}) and Right({ root:6, left: 4, right: 7} ) Children;
                        Inorder Traversal : Node(6)-> {left: 4, right: 7} ------>  Node(4)-> {left: Nil, right: Nil}
                        Next Inorder Successor Node = { root: 4, left: Nil, right: Nil}

        Step4: Replace Node(3) value with Node(4) i.e., { root: 3, left: 1, right: 6} -->  { root: 4, left: 1, right: 6}
               Delete Node(4) in Right(6) subtree
                       ---------------------------------
             STACK:    |   |   |   |   |   |  |  | 8 |
                       ---------------------------------

        Step5: [ 4 < 6 ] -> So, Search Left :: { root: 6, left: 4, right: 7}
                       ---------------------------------
             STACK:    |   |   |   |   |   |   | 6 | 8 |
                       ---------------------------------

        Step6: [ 4 == 4 ] -> Match Found :: { root: 4, left: Nil, right: Nil}
                       ---------------------------------
             STACK:    |   |   |   |   |   | 4 | 6 | 8 |
                       ---------------------------------

        Step7: Both LEFT & RIGHT are Nil, so -> return None (which is LEFT of 6)
                       ---------------------------------
             STACK:    |   |   |   |   |  |  | 6 | 8 |
                       ---------------------------------

        Step4: return { root: 8, left: 4, right: 10}
                       ---------------------------------
             STACK:    |   |   |  |   |   |   |   |    |
                       ---------------------------------

        :param root:
        :param item:
        :return:
        """
        if not root:
            return root

        if item < root.value:
            root.left = self.delete(root.left, item)
        elif item > root.value:
            root.right = self.delete(root.right, item)
        else:
            # Item To Remove
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                root.value = self.inorder_successor(root.right)
                root.right = self.delete(root.right, root.value)
        return root

    @staticmethod
    def inorder_successor(node: TreeNode):
        min_val = node.value
        while node.left:
            min_val = node.left.value
            node = node.left
        return min_val


class RedBlackTree:
    """
        1. Height diff. b/w LEFT vs RIGHT sub trees = [-1, 0 , 1]
        2. ROOT, Leaf(Nil/Null) Nodes are BLACK
        3. For Red Node -> both child nodes must be BLACK
        4. Black Depth :: From any Node, No.of Black Nodes in diff. paths to leaf(NIL) must be SAME

        Left/Right Rotation help(s) in maintaining the above properties
        Left Rotation:

        Note: Max of TWO rotations is enough - Best for Insert/Delete
    """
    pass


class AVLTree:
    pass
