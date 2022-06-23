# The most intuitive method for finding the max sub-array would be to use
# a nested for loop to iterate through the array twice, except for the inner
# array, the loop begins at the index of the outer loop.

# The solution below is more optimal than O(n^3), since we're using a variable
# current_subarr_sum to keep track of the sum of the sub_array, instead of having
# to do another linear scan to add all the elements up:
def maxSubArraySlow(nums):

    # Initialize a max_sum variable, but set it to be the lowest possible
    # value since setting it to zero will yield incorrect result if the
    # arrays are filled with negative numbers:
    max_sum = float("-inf")

    for i in range(len(nums)):

        # At the beginning of each outer loop, we reset the current_subarr_sum
        # which tracks the sum of the current sub-array. This is so that
        # we don't need to perform additional linear scan to add all the
        # elements in the sub-array:
        current_subarr_sum = 0

        for j in range(i, len(nums)):

            # Add current element onto current_subarr_sum
            current_subarr_sum += nums[j]
            # Check if the current_subarr_sum is an improvement to the max_sum:
            max_sum = max(current_subarr_sum, max_sum)

    return max_sum


# The faster approach is to perform a linear scan of the array. As you
# scan each element, we add onto the temporary current_sum value.

# However, if the current_sum value dips below 0 (negative), we can say
# that the sub-array formed before is no longer viable as it would contribute
# negatively to the max_sum value. So instead, we re-set the sub-array to zero,
# which effectively removes the previous elements from the sum and re-starting
# the sub-array from that point.

# RESTART         RESTART       NOT-RESTART          NOT-RESTART
#   [-2,     1,     -3,     4,     -1,     2,     1,     -5,     4]

# Note how we don't re-set the sub-array on every negative element, but only
# if the negative element addition causes the current_sum value to dip below
# negative:
def maxSubArray(nums):

    max_sum = float('-inf')
    current_sum = 0

    for n in nums:
        # If current-sub-array sum dips below zero, reset the left boundary
        # to the current element to negate the effect of previous elements:
        if current_sum < 0:
            current_sum = 0

        # Add current element value to current_sum:
        current_sum += n
        # Compare against the max_sum:
        max_sum = max(max_sum, current_sum)

    return max_sum

