# Two major givens: There is exactly one solution, and we are
# not allowed to use the same element twice.

# Most intuitive way to solve this problem would be to simply
# loop through the array O(n^2) times to calculate all possible
# two sum combinations and see if they meet the target:
def twoSumSlow(nums, target):

    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and i != j:
                return [i, j]


# Efficient solution: From the second hint, we know that we can't
# use the same element twice. We can solve this by only passing
# through the array once, which will give us O(n) solution:
def twoSum(nums, target):

    # Instantiate a dictionary,
    stored = {}

    for i in range(len(nums)):
        current = nums[i]
        remainder = target - current

        if remainder in stored:
            return [i, stored[remainder]]

        stored[nums[i]] = i
