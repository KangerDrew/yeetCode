from collections import deque

# You can use iterative BFS solution to solve this problem, but there is
# a way to solve this using recursive "DFS" solution. You just need to
# keep track of which level you are entering at each recursion stack...


def levelOrderTraversal(root):

    if not root:
        return []

    level_order_res = []
    queue = deque([root])

    while queue:

        current_level = []

        for n in range(len(queue)):

            current_node = queue.popleft()

            if current_node:
                current_level.append(current_node.val)
                queue.append(current_node.left)
                queue.append(current_node.right)

        if current_level:
            level_order_res.append(current_level)

    return level_order_res

