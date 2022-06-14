# My first attempt:
# I re-cycled my first attempt from validateBST problem, where I create
# inorder array, and instead of checking the order, return the kth smallest
# element in that sorted array (assuming all inputs are valid BST):
def kthSmallest(root, k):
    # Create array
    inorder = []

    def dfsInorder(node):
        # Only append when node is not null:
        if node:
            # Recursively enter left node:
            dfsInorder(node.left)
            # Then append current node:
            inorder.append(node.val)
            # Finally, recursively enter right node:
            dfsInorder(node.right)

    # Call helper function:
    dfsInorder(root)

    # Return the kth smallest element (k - 1 index)
    return inorder[k - 1]
