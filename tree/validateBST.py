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


def isValidBSTShorter(root):

    # The helper function will return False if the boundaries do not
    # meet the requirement for Binary Search Tree
    def valid(node, left, right):
        # Base Case: If we reach below the leaf node without
        # returning false, it means we've met the requirement
        # for BST for that recursion stack
        if not node:
            return True

        # Below is a scenario where left child is larger than current node,
        # and right child is less than the current node (invalid BST):
        if not right > node.val > left:
            return False

        # Recursively check if the left and right nodes meet the BST requirement.
        # The boundary for left - right node cannot be larger than current node
        # The boundary for right - left node cannot be smaller than current node
        return valid(node.left, left, node.val) and valid(node.right, node.val, right)

    # Initialize the recursion, using -inf for left boundary and +inf for right boundary:
    return valid(root, float('-inf'), float('inf'))
