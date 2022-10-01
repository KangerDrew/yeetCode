# House robber 2 problem states that now the provided "houses" are
# in circle, so we can no longer rob the first house AND the last house.

# Solution to this is to simply perform the function from the first variant
# problem (houseRobber) twice - once on the array without the last value, and
# again on the array without the first value. Then, we compare the two results
# and take the largest between the two.

def houseRobber2(nums):

    def helper(arr):
        rob1, rob2 = 0, 0

        for n in arr:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

    # Edge case: if there's only 1 house to rob, just rob it:
    if len(nums) == 1:
        return nums[0]

    return max(helper(nums[1:]), helper(nums[:-1]))
