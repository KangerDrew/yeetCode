# There are more clever ways to solve this using object reference
# but this was my first attempt.
def pathSumII(root, targetSum):
    resString = []
    res = []

    def dfs(node, currentSum, currentSumStr):

        if not node:
            return None

        if not node.left and not node.right:
            currentSum += node.val
            currentSumStr += str(node.val)

            if currentSum == targetSum:
                resString.append(currentSumStr)

            return None

        currentSum += node.val
        currentSumStr += str(node.val) + ","

        dfs(node.left, currentSum, currentSumStr)
        dfs(node.right, currentSum, currentSumStr)

    dfs(root, 0, "")

    for sumString in resString:
        res.append(sumString.split(","))

    return res