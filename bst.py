class Node:
    def __init__(self, value):
        self.key = value
        self.parent = None
        self.left_child = None
        self.right_child = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
        else:
            current_node = self.root
            while True:
                if value < current_node.key:
                    if current_node.left_child is None:
                        current_node.left_child = node
                        node.parent = current_node
                        break
                    current_node = current_node.left_child
                else:
                    if current_node.right_child is None:
                        current_node.right_child = node
                        node.parent = current_node
                        break
                    current_node = current_node.right_child
        return node

    def inorder_tree_walk(self, node):
        if node is not None:
            inorder_tree_walk(node.left)
            print node.key
            inorder_tree_walk(node.right)
