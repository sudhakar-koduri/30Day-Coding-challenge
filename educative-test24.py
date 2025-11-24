# Definition for a binary tree node
class EduTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

# from EduTreeNode import *

def lowest_common_ancestor(p, q):
    p_parents_stack = []
    node = p
    while node :
        p_parents_stack.append(node.data)
        node = node.parent

    node = q 
    while node:
        if node.data in p_parents_stack:
            return node
        node = node.parent
    # Return the root node - since the constraint that P and Q are on same tree.
    return p_parents_stack.pop()

# LCA using smart two-pointer approach - Ideal solution
def lowest_common_ancestor(p, q):
    # Initialize two pointers
    ptr1, ptr2 = p, q

    # Traverse until they meet
    while ptr1 != ptr2:

        # Move ptr1 to parent node or switch to the other node if reached the root
        if ptr1.parent:
            ptr1 = ptr1.parent
        else:
            ptr1 = q

		# Move ptr2 to parent node or switch to the other node if reached the root
        if ptr2.parent:
            ptr2 = ptr2.parent
        else:
            ptr2 = p

    # Return ptr1 or ptr2, since they are the same at this point
    return ptr1