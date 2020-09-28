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
        if value < self.value:
        # check if the new node's value is less than the current node value.
            if self.left:
            # if there is already another node on the left, run the insert function
            # recursively on the left node.
                return self.left.insert(value)
            else:
            # otherwise - create a new node and assign it as left child.
                self.left = BSTNode(value)
                return True
        else:
        # do the same on the right node, if the new node value is equal or greater than
        # the current node value.
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BSTNode(value)
                return True

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
        # if the value of the current node matches target - return True
            return True
        else:
            if target < self.value and self.left:
            # if the target is lesser than current node, and there is a left child
            # run the contians method on the left node.
                return self.left.contains(target)
            elif target > self.value and self.right:
            # same logic on the right node.
                return self.right.contains(target)
            else:
            # if there is no child nodes, we reached the leaf node and 
            # didn't find the value. Return False.
                return False