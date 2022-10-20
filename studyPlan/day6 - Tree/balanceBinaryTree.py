# Use depth first search algorithm (iterative is probably faster)
# that keeps track of the current height of the node, and whether
# the tree is balanced or not


def balancedBinaryTree(root):

    def dfs(node):

        if not node:
            return [0, True]

        res_left = dfs(node.left)
        res_right = dfs(node.right)

        balanced = (abs(res_left[0] - res_right[0]) <= 1) and (res_left[1] and res_right[1])
        current_height = max(res_left[0], res_right[0]) + 1

        return [current_height, balanced]

    final_res = dfs(root)
    return final_res[1]
