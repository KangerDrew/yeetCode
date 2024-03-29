import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# The approach for this problem is to use a HashMap that keeps track of
# "the prefix sum". The prefix sum in binary tree is the list of continuous
# sum from the root to the leaf node, where at each new level you keep track
# of what the current total sum of the nodes traversed are.

# At each level, we'll keep track of what the currentSum value is, and record
# how many times that currentSum value has occurred during that traversal,
# using a HashMap.

# The prefix sum list (we'll be using dictionary to keep track of this) will
# allow us to check for two following scenarios:

# Scenario 1) The targetSum is reached by summing all the traversed nodes
# Scenario 2) The targetSum CAN be reached, if we remove some nodes at the
# beginning of the summed nodes.

# Scenario 1 is easy enough to determine as we traverse down the tree. For
# scenario 2 however, we can check by subtracting the currentSum from the
# targetSum value, and see if that leftover value was recorded during the
# traversal...


def pathSumIII(root, targetSum):
    count = 0
    h = collections.defaultdict(int)

    def preorder(node, curr_sum):
        nonlocal count
        if not node:
            return
        curr_sum += node.val

        if curr_sum == targetSum:
            count += 1

        count += h[curr_sum - targetSum]
        h[curr_sum] += 1

        preorder(node.left, curr_sum)
        preorder(node.right, curr_sum)

        h[curr_sum] -= 1

    preorder(root, 0)
    return count


# Example for debugging:
head = TreeNode(10)
head.left = TreeNode(5)
head.left.left = TreeNode(3)
head.left.left.right = TreeNode(-2)
head.left.left.left = TreeNode(0)
head.left.left.left.left = TreeNode(0)

head.left.right = TreeNode(2)
head.left.right.right = TreeNode(1)

head.right = TreeNode(-3)
head.right.right = TreeNode(11)

print(pathSumIII(head, 8))


def pathSumIIIMod(root, targetSum):
    h = collections.defaultdict(int)

    def preorder(node, curr_sum, count):

        if not node:
            return count

        curr_sum += node.val

        count += h[curr_sum - targetSum]

        if curr_sum == targetSum:
            count += 1

        h[curr_sum] += 1
        count = preorder(node.left, curr_sum, count)
        count = preorder(node.right, curr_sum, count)
        h[curr_sum] -= 1

        return count

    return preorder(root, 0, 0)


print(pathSumIIIMod(head, 8))


def pathSumIIIdiff(root, targetSum):
    h = collections.defaultdict(int)

    def preorder(node, curr_sum):

        if not node:
            return 0

        curr_sum += node.val

        count = h[curr_sum - targetSum]

        if curr_sum == targetSum:
            count += 1

        h[curr_sum] += 1
        count += preorder(node.left, curr_sum)
        count += preorder(node.right, curr_sum)
        h[curr_sum] -= 1

        return count

    return preorder(root, 0)


# print(pathSumIIIdiff(head, 8))

# Another example from notes:
newHead = TreeNode(0)
newHead.left = TreeNode(0)
newHead.left.left = TreeNode(0)
newHead.left.left.left = TreeNode(8)
newHead.left.left.left.left = TreeNode(-8)
newHead.left.left.left.left.left = TreeNode(8)
print(pathSumIIIdiff(newHead, 8))
print(pathSumIIIMod(newHead, 8))
