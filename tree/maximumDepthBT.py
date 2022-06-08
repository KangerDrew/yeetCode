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


# Iterative DFS solution. This works bit differently than the recursive DFS solution,
# since we need some way to keep track of the depth of each node:
def maximumDepthItrDFS(root):

    if not root:
        return 0

    # As mentioned in the description, we need some way to keep track of the
    # depth of each node. To do this, we'll just use a length 2 array (list)
    # where array[0] is the node, and array[1] is the depth of the node:
    stack = [[root, 1]]
    # Define a variable to keep track of the max depth:
    max_depth = 1

    while stack:

        # Remove (pop off the stack) the last element from stack:
        node, current_depth = stack.pop()

        # Below if statement only executes if node is not None.
        # This is because, if node.left is None (null node),
        # the "depth" value of the null node shouldn't be considered
        # since it's invalid:
        if node:
            # Take the largest value between max_depth and current_depth:
            max_depth = max(max_depth, current_depth)

            # Append two child node of the current node. As mentioned,
            # if either of the nodes are null, the if statement will
            # not consider that depth value:
            stack.append([node.left, current_depth + 1])
            stack.append([node.right, current_depth + 1])

    return max_depth

