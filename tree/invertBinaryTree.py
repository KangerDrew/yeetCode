def invertTreeRecur(root):
    # Edge case: in case we get null node
    if not root:
        return None

    # Store original left and right nodes:
    left = root.left
    right = root.right

    # Take the stored values and invert them:
    root.left = right
    root.right = left

    # Recursively do the same for left and right node:
    invertTreeRecur(root.left)
    invertTreeRecur(root.right)

    return root

