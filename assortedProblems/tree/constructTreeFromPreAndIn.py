# Think like dynamic programming approach (even though this is not
# a Dynamic Programming problem), where you try to split the given
# information into smaller pieces:

# Pre-order: center, left, right node traversal
# The first value in the pre-order list is the root node
# of that given tree.

# In-order: left, center, right node traversal
# The first value in the in-order list is the leftmost value
# of the given tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None

    # As mentioned before, the first value of preorder list
    # is going to be the root of the tree:
    root_val = preorder[0]

    # Create root node:
    root = TreeNode(root_val)

    # Then, we need to locate the root value within the inorder
    # array. It was given that the values in both arrays are
    # unique, so simply return the index when the value is matched:

    inorder_root_index = 0
    while inorder[inorder_root_index] != root_val:
        inorder_root_index += 1

    # For inorder list, elements left to the inorder_root_index will all belong to the left subtree.
    # For preorder list, elements left to 1 + inorder_root_index, excluding the root value itself will
    # belong to the left subtree.

    # The remaining content (not including the root value itself) will all belong to the right subtree!
    # See https://youtu.be/ihj4IQGZ2zc?t=230 for visual explanation:
    root.left = buildTree(preorder[1:inorder_root_index + 1], inorder[:inorder_root_index])
    root.right = buildTree(preorder[inorder_root_index + 1:], inorder[inorder_root_index + 1:])

    return root
