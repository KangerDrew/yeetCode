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

    # create stack
    stack = []
    current = root

    while current or stack:

        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        k -= 1

        if k == 0:
            return current.val

        current = current.right


two = TreeNode(2)
one = TreeNode(1, None, two)
four = TreeNode(4)
three = TreeNode(3, one, four)

print(kthSmallestItr(three, 1))
