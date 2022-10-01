class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


def kthSmallestItr(root, k):

    # create stack, and current node pointer
    stack = []
    current = root

    while current or stack:

        # The nested while loop below will only run when we are
        # seeking the leftmost node from the current node:
        while current:
            stack.append(current)
            current = current.left

        # Remove the most recent entry from stack:
        current = stack.pop()
        # Decrement k value by 1:
        k -= 1

        # If we reached k = 0, it means that the current.val
        # is the kth smallest element:
        if k == 0:
            return current.val

        # If above if statement return didn't trigger, it means
        # we need to traverse deeper into right, or pop back to the parent node.

        # 1) If former is true, setting current to current.right will do exactly that

        # 2) If the latter is true, setting current to current.right (which should be null)
        # will cause the nested while loop at the beginning to skip over, and have the
        # main while loop execute current = stack.pop() immediately. The latest node in stack
        # should be the parent of the current node!
        current = current.right

