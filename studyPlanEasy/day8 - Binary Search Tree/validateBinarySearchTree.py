# Simply check if all left children of the current node is smaller in value, and right
# children are greater in value. You can solve this both recursively, and iteratively:

def validateBST(root):

    def helper(node, l_bound, r_bound):
        # Reached the root without returning False, return True:
        if not node:
            return True

        # Check if current node is within expected range:
        if not (l_bound < node.val < r_bound):
            return False

        # Recursively traverse down both left and right, while adjusting
        # their boundaries. If either returns False, we know that this is
        # not a valid BST:
        return helper(node.left, l_bound, node.val) and helper(node.right, node.val, r_bound)

    return helper(root, float('-inf'), float('inf'))
