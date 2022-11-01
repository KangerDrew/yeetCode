# First attempt:
import collections

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def preorder(root):

    def dfs(node):
        if not node:
            return []

        res = [node.val]

        for c in node.children:
            res_c = dfs(c)
            res.extend(res_c)

        return res

    return dfs(root)


# My attempt at iterative solution:
def preorder(root):
    if not root:
        return []

    res = []
    stack = collections.deque([root])

    while stack:

        current = stack.pop()
        res.append(current.val)

        for i in range(len(current.children) - 1, -1, -1):
            stack.append(current.children[i])

    return res
