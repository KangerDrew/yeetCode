from collections import deque
# Note: for level order traversal, we each leve can contain
# more than 2 nodes (not very clear from examples)
def levelOrderTrav(root):
    if not root:
        return []

    # use python's deque:
    queue = deque([root])
    # Keep track of the total level order:
    level_order = []

    while queue:
        # We will be using BFS to traverse each level one by one:
        current_level = []

        # With each iteration of while loop, we process all the
        # content in the queue, since each while loop should populate
        # queue with all the nodes in one level:
        for i in range(len(queue)):
            node = queue.popleft()
            # Only process the node if it's not null:
            if node:
                current_level.append(node.val)
                # Append its children to the queue:
                queue.append(node.left)
                queue.append(node.right)

        # We need this if statement, because the for loop above will
        # also append (but not process) a null nodes below our final level:
        if current_level:
            level_order.append(current_level)

    return level_order
