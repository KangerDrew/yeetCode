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

    # Instantiate a dictionary (hash map), where we'll store the
    # num value as key, and its index (position) as the value.

    # The reason why we're using the num value as key is because
    # it is much faster to search if a key exists in hash maps,
    # rather than its value:
    stored = {}

    for i in range(len(nums)):
        # Get the current value using current index i:
        current = nums[i]
        # Determine how much value is required for us to
        # reach the target sum value:
        remainder = target - current

        # Check if the remainder was already stored in the dictionary.
        # As mentioned before, we configured the dictionary such that
        # the num value is the key of the dictionary:
        if remainder in stored:
            # If true, we return the index, and the remainder's key-value:
            return [i, stored[remainder]]

        # Otherwise, store the current num value (as key) and index (as value):
        stored[nums[i]] = i
