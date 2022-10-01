from collections import deque

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


def invertTreeItrBFS(root):
    # Edge case: in case we get null node
    if not root:
        return None

    queue = deque([root])

    while queue:
        current = queue.popleft()

        # Check if current node is leaf node. If yes, skip it:
        if not current:
            continue

        # # Use single temp variable for switching:
        # temp = current.left
        #
        # current.left = current.right
        # current.right = temp

        # One liner for switching left and right:
        current.left, current.right = current.right, current.left

        # Add left and right node to queue:
        queue.append(current.left)
        queue.append(current.right)

    return root

