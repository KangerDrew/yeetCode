# This is definitely not an easy problem... lol

# The diameter is defined as "length of the longest path between
# any two nodes in a tree, and the path doesn't have to cross
# the root". Another way to interpret this is the sum of the
# max depth of left node and right node!

def diameterOfBinaryTree(root):

    diameter = 0

    def dfs(node):

        # Base case - return 0 if we're at null node:
        if not node:
            return 0

        # Get the max depths from left and right tree:
        left = dfs(node.left)
        right = dfs(node.right)

        # Update the diameter value, if the diameter of current
        # node is greater:
        nonlocal diameter
        diameter = max(diameter, left + right)

        # return the max depth, either 1 + left or 1 + right:
        return 1 + max(left, right)

    # Run dfs on root:
    dfs(root)
    # dfs(root) should have updated the diameter function. Return it:
    return diameter

