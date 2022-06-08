from collections import deque
# Solution using recursive DFS function:
def maximumDepthRecursiveDFS(root):

    # We don't need a nested function, but I did it here
    # so I can easily paste the solution into online editor:
    def dfs(node):
        # Base Case #1: return 0 if None is the input
        if not node:
            return 0

        # Base Case #2: return 1 if current node doesn't have any children:
        if not node.left and not node.right:
            return 1

        # Final Case: Recursively calculate the depth value of node.left, and
        # node.right, take the max between the two, and increment by 1 to get
        # the max depth value:
        return max(dfs(node.left), dfs(node.right)) + 1

    return dfs(root)


# Iterative BFS solution. We use a deque as a queue DS, where we increment a counter by
# one each time we reach a new level:
def maximumDepthItrBFS(root):

    if not root:
        return 0

    # Initialize a depth variable:
    depth = 0

    # Use python's deque():
    queue = deque([root])

    while queue:
        # On each iteration of the while loop, we are going down
        # the depth of the tree. The for loop below will remove
        # all the nodes in the current level, and add their children
        # into the queue structure (if they exist):
        for i in range(len(queue)):
            # Take the node from the beginning of queue
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # All nodes on next level have been added to queue,
        # so we can increment depth by 1:
        depth += 1

    return depth
