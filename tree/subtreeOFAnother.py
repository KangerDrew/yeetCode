# My attempt at subtree of another problem:
def isSubtree(root, subRoot):
    # Base case: We reached the end of tree without a match
    if not root:
        return False

    # We use DFS algorithm to traverse the tree:
    def dfsCheck(node1, node2):
        # Base case: We successfully traversed the tree
        # without a False return
        if not node1 and not node2:
            return True

        # After the first if condition, below if statement
        # checks to see if only one of the node is Null
        # Return False if so:
        if not node1 or not node2:
            return False

        # Check if the values are not matching:
        if node1.val != node2.val:
            return False

        # Finally, run the dfsCheck recursively on the left side of the tree and
        # right side of the tree. Both must return True for subtree to match:
        return dfsCheck(node1.left, node2.left) and dfsCheck(node1.right, node2.right)

    # If the current root value and subRoot value match, we run dfsCheck to see if
    # the subRoot and current root have the same children:
    if root.val == subRoot.val and dfsCheck(root, subRoot):
        return True

    # Otherwise, recursively call isSubtree function on left and right side to see
    # if a match turns up:
    return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

