# Think like dynamic programming approach (even though this is not
# a Dynamic Programming problem), where you try to split the given
# information into smaller pieces:

# Pre-order: center, left, right node traversal
# In-order: left, center, right node traversal


def buildTree(preorder, inorder):
    if not preorder or inorder:
        return None
