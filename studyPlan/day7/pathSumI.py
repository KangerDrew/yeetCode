def pathSum(root, targetSum):

    def dfs(node, currentSum):
        if not node:
            return False

        currentSum += node.val

        if not node.left and not node.right:
            return currentSum == targetSum

        return dfs(node.left, currentSum) or dfs(node.right, currentSum)

    return dfs(root, 0)