import collections

# My attempt:
# To validate a Binary Search Tree (BST), we can generate inorder traversal
# list. BST's inorder traversal list MUST be order from smallest to largest!

# THIS SOLUTION FAILED. dfsInorder function is incorrect.
def isValidBST(root):

    inorder = collections.deque()

    def dfsInorder(node):
        # Base condition #1: append leaf node
        if not node.left and not node.right:
            inorder.append(node.val)
            return None

        # if first if statement didn't trigger, it means
        # one of the nodes might be null. Check if left
        # node exists. Recursively enter it if it does:
        if node.left:
            inorder.append(dfsInorder(node.left))
            return None

        # Once left node is appended, we need to append
        # the node value itself
        if not node.left:
            inorder.append(node.val)
            return None

        # Append the right node value:
        if node.right:
            inorder.append(dfsInorder(node.right))
            return None

    dfsInorder(root)

    # My attempt at validating the elements are in order... ALSO INCORRECT:
    while inorder:
        prev, after = inorder.popleft(), inorder.popleft()

        if prev > after:
            return False

    # return True if above loop doesn't return False:
    return True


# Corrected solution, helper function now properly appends values
# to the inorder deque:
def isValidBSTCORRECTED(root):

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

    # Use for loop to check if elements are in order:
    for i in range(1, len(inorder)):
        if inorder[i] <= inorder[i - 1]:
            return False

    # return True if above loop doesn't return False:
    return True
