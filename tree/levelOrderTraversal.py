from collections import deque
# Note: for level order traversal, we each leve can contain
# more than 2 nodes (not very clear from examples)
def levelOrderTrav(root):
    if not root:
        return []

    # use python's deque:
    queue = deque([root])
    level_order = []

    while queue:

        current_level = []

        for i in range(len(queue)):
            node = queue.popleft()
            if node:
                current_level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

        if current_level:
            level_order.append(current_level)

    return level_order
