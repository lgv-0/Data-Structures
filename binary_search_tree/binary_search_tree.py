"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        new_node = BSTNode(value)

        relative_node = None
        hunt_node = self
        while relative_node is None:
            if hunt_node.value > value:
                if hunt_node.left is not None:
                    hunt_node = hunt_node.left
                else:
                    relative_node = hunt_node
            else:
                if hunt_node.right is not None:
                    hunt_node = hunt_node.right
                else:
                    relative_node = hunt_node

        if relative_node.value < value:
            relative_node.right = new_node
        else:
            relative_node.left = new_node

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        def seek(cur_node):
            if cur_node.value is target:
                return True

            if cur_node.value > target:
                if cur_node.left is None:
                    return False
                else:
                    return seek(cur_node.left)
            elif cur_node.value < target:
                if cur_node.right is None:
                    return False
                else:
                    return seek(cur_node.right)

        return seek(self)

    # Return the maximum value found in the tree
    def get_max(self):
        max = self.value

        def seek(cur_node):
            nonlocal max

            if (cur_node.value > max):
                max = cur_node.value
            
            if cur_node.left is not None:
                seek(cur_node.left)
            if (cur_node.right is not None):
                seek(cur_node.right)

        seek(self)

        return max

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        def foreach(cur_node):
            fn(cur_node.value)

            if cur_node.left is not None:
                foreach(cur_node.left)
            if (cur_node.right is not None):
                foreach(cur_node.right)

        foreach(self)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

bst = BSTNode(12)
bst.insert(7)
bst.insert(14)
bst.insert(5)
bst.insert(9)
bst.insert(13)
bst.insert(21)
bst.insert(22)
bst.insert(24)
bst.insert(25)
bst.insert(26)
print(bst.contains(24))
print(bst.get_max())
bst.for_each(print)