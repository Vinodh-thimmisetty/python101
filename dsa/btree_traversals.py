from dsa.utils import TreeNode, height_of_tree


class BinaryTree:

    def __init__(self):
        self.nodes = []

    # IN-ORDER (DFS)
    def left_root_right(self, root: TreeNode):
        if root:
            self.left_root_right(root.left)
            self.nodes.append(root.value)
            self.left_root_right(root.right)

    # PRE-ORDER (DFS)
    def root_left_right(self, root: TreeNode):
        if root:
            self.nodes.append(root.value)
            self.root_left_right(root.left)
            self.root_left_right(root.right)

    # POST-ORDER (DFS)
    def left_right_root(self, root: TreeNode):
        if root:
            self.left_right_root(root.left)
            self.left_right_root(root.right)
            self.nodes.append(root.value)

    # LEVEL-ORDER RECURSIVE (BFS)
    def level_order_traversal(self, root: TreeNode):
        tree_height = height_of_tree(root)
        for level in range(1, tree_height + 1):
            self.read_level(root, level)

    # LEVEL-ORDER ITERATIVE (BFS)
    def level_order_traversal_iterative(self, root: TreeNode):
        temp_nodes = [root]
        while len(temp_nodes) > 0:
            cur_node = temp_nodes.pop(0)
            self.nodes.append(cur_node.value)
            if cur_node.left:
                temp_nodes.append(cur_node.left)
            if cur_node.right:
                temp_nodes.append(cur_node.right)

    def read_level(self, root, level):
        if not root:
            return
        if level == 1:
            self.nodes.append(root.value)
        else:
            self.read_level(root.left, level - 1)
            self.read_level(root.right, level - 1)
