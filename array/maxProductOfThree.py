# Problem link: https://leetcode.com/problems/maximum-product-of-three-numbers/

# The solution is simple - find the two smallest values in the array, and find
# the three largest values as well. The maximum product of three would either be
# the product of two smallest values and the largest value (-)*(-)*(+), or the
# product of three largest values (+)*(+)*(+):
def maximumProduct(nums):
    min_1, min_2 = float('inf'), float('inf')
    max_1, max_2, max_3 = float('-inf'), float('-inf'), float('-inf')

    # min_1 < min_2 < max_3 < max_2 < max_1

    for n in nums:
        if n <= min_1:
            min_2 = min_1
            min_1 = n;
        elif n <= min_2:
            min_2 = n

        if n >= max_1:
            max_3 = max_2
            max_2 = max_1
            max_1 = n
        elif n >= max_2:
            max_3 = max_2
            max_2 = n
        elif n >= max_3:
            max_3 = n

    return max(min_1 * min_2 * max_1, max_1 * max_2 * max_3)


# Same principle as the ideal solution, but instead of doing the linear scan of
# the array, we sort it to find the two lowest values and three largest values:
def maximumProductSlower(nums):

    nums.sort()

    return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
