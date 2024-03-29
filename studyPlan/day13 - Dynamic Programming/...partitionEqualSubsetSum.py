import collections
# When we calculate the total sum, we need to ensure that we can  create a
# sub-array that can reach half the total sum. This means that the remaining
# value(s) will form another sub-array who's sum will be half the total sum!

# If total sum is odd value, and our values only consist of integers, we can't
# get sub-array who's sum is half the total sum!


def partitionEqualSum(nums):
    total = sum(nums)

    # If the total is non-even, it is impossible to create two sub-arrays
    # of same values...
    if total % 2 != 0:
        return False

    target = total // 2
    # Initialize a set that'll keep track of all possible sum values:
    all_sums = set()

    for n in nums:

        # Create a new set that'll replace the current all_sums set:
        new_all_sums = set()

        # Check if the value itself is the sum. If so, return True:
        if n == target:
            return True

        # Add the current n value to the new_all_sums:
        new_all_sums.add(n)

        # Loop through every possible sum values we've gotten so far:
        for s in all_sums:

            # If the combination of the s and n is the target, return True:
            if s + n == target:
                return True
            # If the combination exceeds target, we don't need to add it to
            # the set (optimization). Just add the s and skip to next loop:
            elif s + n > target:
                new_all_sums.add(s)
                continue

            # If neither occurred above, just add the combination:
            new_all_sums.add(s + n)
            # Remember to ALSO add the s into the new_all_sums (need to add
            # it back to all_sums):
            new_all_sums.add(s)

        # Set all_sums to new_all_sums:
        all_sums = new_all_sums

    # Check if the target is in all_sums after the loop above:
    return True if target in all_sums else False


# print(partitionEqualSum([1, 5, 11, 5]))
# test = [0, 1, 2, 3, 4]
# print(test[0:2] + test[5:-1])


# Recursive solution (not mine)
def partitionRecur(nums):

    @lru_cache(maxsize=None)
    def dfs(nums: Tuple[int], n: int, subset_sum: int) -> bool:
        # Base cases
        if subset_sum == 0:
            return True
        if n == 0 or subset_sum < 0:
            return False
        result = (dfs(nums, n - 1, subset_sum - nums[n - 1])
                  or dfs(nums, n - 1, subset_sum))
        return result

    # find sum of array elements
    total_sum = sum(nums)

    # if total_sum is odd, it cannot be partitioned into equal sum subsets
    if total_sum % 2 != 0:
        return False

    subset_sum = total_sum // 2
    n = len(nums)
    return dfs(tuple(nums), n - 1, subset_sum)

