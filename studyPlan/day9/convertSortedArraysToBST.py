class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# We can recursively solve this problem (keep track of left & right boundary)


def sortedToBST(nums):

    def dfs(left_bound, right_bound):

        if left_bound > right_bound:
            return None

        mid_point = left_bound + (right_bound - left_bound) // 2

        center = TreeNode(nums[mid_point])

        center.left = dfs(left_bound, mid_point - 1)
        center.right = dfs(mid_point + 1, right_bound)

        return center

    return dfs(0, len(nums) - 1)
