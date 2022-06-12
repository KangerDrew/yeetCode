# My attempt at subtree of another problem:
def isSubtree(root, subRoot):
    if not root:
        return False

    def dfsCheck(node1, node2):
        if not node1 and not node2:
            return True

        if not node1 or not node2:
            return False

        if node1.val != node2.val:
            return False

        return dfsCheck(node1.left, node2.left) and dfsCheck(node1.right, node2.right)

    if root.val == subRoot.val and dfsCheck(root, subRoot):
        return True

    return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)