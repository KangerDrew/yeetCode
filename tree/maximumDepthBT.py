# Below is a solution using recursive DFS function:
def maximumDepthRecursiveDFS(root):

    def dfs(node):
        if not node:
            return 0

        if not node.left and not node.right:
            return 1

        return max(dfs(node.left), dfs(node.right)) + 1

    return dfs(root)

