class Node:
    """
    Implementation of a Node
    ========================
    Each node has its key (k), parent(p), left child (l) and right child (r) as seen in the following diagram:
            p
           /\
          /  \
          k  ..
         /\
        /  \
       l    r
    The parent and children are also nodes, the key is a value (integer, float etc.)
    """
    def __init__(self, value):
        self.key = value
        self.parent = None
        self.left_child = None
        self.right_child = None

class BST:
    """
    Implementation of a Binary Search Tree
    ======================================
    This is that actual implementation of the tree using the node class to represent the nodes of the tree.
    """
    def __init__(self):
        self.root = None

    def insert(self, value):
        # Inserts a value into the tree as a new node
       
        
        if isinstance(value, (int, float, long)): # Make sure it's a number    
            node = Node(value) # Initialise a node with the correct value
            if self.root is None:
                self.root = node # Tree is empty so insert first node
            else:
                current_node = self.root
                while True:
                    if value < current_node.key:
                        # Go left if value is less than the current node key
                        if current_node.left_child is None:
                            # Node goes here if there is no left child
                            current_node.left_child = node
                            node.parent = current_node
                            break
                        current_node = current_node.left_child
                    else:
                        # Go right
                        if current_node.right_child is None:
                            # Node goes here if there is no right child
                            current_node.right_child = node
                            node.parent = current_node
                            break
                        current_node = current_node.right_child
            print("Inserted " + str(value) + " into BST successfully.")
        else:
            print("Please enter a (non-complex) number")

    def inorder_tree_walk(self, node):
        # Sorts the tree in ascending order
        if node is None:
            return
        else:
            self.inorder_tree_walk(node.left_child)
            print node.key
            self.inorder_tree_walk(node.right_child)

    # Print the tree... not my implementation
    def __str__(self):
        if self.root is None: return '<empty tree>'
        def recurse(node):
            if node is None: return [], 0, 0
            label = str(node.key)
            left_lines, left_pos, left_width = recurse(node.left_child)
            right_lines, right_pos, right_width = recurse(node.right_child)
            middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
            pos = left_pos + middle // 2
            width = left_pos + middle + right_width - right_pos
            while len(left_lines) < len(right_lines):
                left_lines.append(' ' * left_width)
            while len(right_lines) < len(left_lines):
                right_lines.append(' ' * right_width)
            if (middle - len(label)) % 2 == 1 and node.parent is not None and node is node.parent.left_child and len(label) < middle:
                label += '.'
            label = label.center(middle, '.')
            if label[0] == '.': label = ' ' + label[1:]
            if label[-1] == '.': label = label[:-1] + ' '
            lines = [' ' * left_pos + label + ' ' * (right_width - right_pos), ' ' * left_pos + '/' + ' ' * (middle-2) + '\\' + ' ' * (right_width - right_pos)] + [left_line + ' ' * (width - left_width - right_width) + right_line for left_line, right_line in zip(left_lines, right_lines)]
            return lines, pos, width
        return '\n'.join(recurse(self.root) [0])
