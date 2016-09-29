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
        self.height = 0

    # Print the node
    def __str__(self):
        # Find left node value
        if self.left_child is None:
            left = " "
        else:
            left = str(self.left_child.key)
        
        # Find right node value
        if self.right_child is None:
            right = " "
        else:
            right = str(self.right_child.key)

        # Draw node with children
        string = " (" + str(self.key) + ")\n"
        string += " / \ \n"
        string += " " + left + " " + right

        # Draw parent if it exists
        if self.parent is not None:
            if self.key < self.parent.key:
                string = "   " + str(self.parent.key) + "\n  /\n" + string
            else:
                string = " " + str(self.parent.key) + "\n  \ \n" + string
        
        return string

default = object()

class BST:
    """
    Implementation of a Binary Search Tree
    ======================================
    This is that actual implementation of the tree using the node class to represent the nodes of the tree.
    """
    def __init__(self):
        self.root = None

    # Inserts a value into the tree as a new node
    def insert(self, value, return_node=False):
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
            if return_node == False:
                return
            else:
                return node
        else:
            print("Couldn't insert " + str(value) + ". Please enter a (non-complex) number")

    # Insert an array of values into the tree
    def insert_array(self, values):
        for x in values:
            self.insert(x)
        print self

    # Sorts the tree in ascending order
    def inorder_tree_walk(self, node=default):
        if node is default:
            node = self.root

        if node is None: # Finished
            return
        else:
            self.inorder_tree_walk(node.left_child) # Go all the way left
            print node.key # Print the value
            self.inorder_tree_walk(node.right_child) # Go right

    # Searches tree for a particular value and prints the node
    def search(self, value, node=default, return_node=False):
        if node is default:
            node = self.root

        # Didn't find the value
        if node is None:
            print("Value not found")
            return node

        # Found the value
        if value == node.key:
            if return_node == False:
                print node
                return
            else:
                return node
        
        # The search part
        if value < node.key:
            return self.search(value, node.left_child, return_node)
        else:
            return self.search(value, node.right_child, return_node)
    
    # Search iteratively
    def search_iteratively(self, value, node=default, return_node=False):
        if node is default:
            node = self.root
        current_node = node
        while current_node is not None:
            if value == current_node.key:
                if return_node == False:
                    print node
                    return
                else:
                    return current_node
            elif value < current_node.key:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        
    # Find the maximum
    def maximum(self, node=default, return_node=False):
        if node is default:
            node = self.root

        while node.right_child is not None:
            node = node.right_child
        if return_node == False:
            print node.key
        else:
            return node

    # Find the minimum
    def minimum(self, node=default, return_node=False):
        if node is default:
            node = self.root

        while node.left_child is not None:
            node = node.left_child
        if return_node == False:
            print node.key
        else:
            return node

    # Given a node, find the successor i.e. next greatest value
    def successor(self, key, return_node=False):
        node = self.search(key, self.root, True)
        if node is None:
            print(str(key) + " was not found in tree")
            return

        if node.right_child is not None:
            return self.minimum(node.right_child, return_node)

        parent_node = node.parent
        while parent_node is not None and node == parent_node.right_child:
            node = parent_node
            parent_node = parent_node.parent
        if parent_node is None:
            if return_node == False:
                print("Node has no succesor")
                return
            else:
                return None
        else:
            if return_node == False:
                return parent_node.key
            else:
                return parent_node

    # Given a node, find the predecessor i.e. next value less than the given node
    def predecessor(self, key, return_node=False):
        node = self.search(key, self.root, True)
        if node is None:
            print(str(key) + " was not found in tree")
            return

        if node.left_child is not None:
            return self.maximum(node.left_child, return_node)

        parent_node = node.parent
        while parent_node is not None and node == parent_node.left_child:
            node = parent_node
            parent_node = parent_node.parent

        if parent_node is None:
            if return_node == False:
                print("Node has no predecessor")
                return
            else:
                return None
        else:
            if return_node == False:
                return parent_node.key
            else:
                return parent_node
            
    # Replace subtree as child of its parent with another subtree
    def transplant(self, node1, node2):
        if node1.parent is None:
            self.root = node2
        elif node1 is node1.parent.left_child:
            node1.parent.left_child = node2
        else:
            node1.parent.right_child = node2

        if node2 is not None:
            node2.parent = node1.parent

    # Delete a node
    def delete(self, node):
        if node.left_child is None:
            self.transplant(node, node.right_child)
        elif node.right_child is None:
            self.transplant(node, node.left_child)
        else:
            node_min = self.minimum(node.right_child, True)
            if node_min.parent is not node:
                self.transplant(node_min, node_min.right_child)
                node_min.right_child = node.right_child
                node_min.right_child.parent = node_min
            self.transplant(node, node_min)
            node_min.left_child = node.left_child
            node_min.left_child.parent = node_min

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
