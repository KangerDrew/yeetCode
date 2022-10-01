# Helper function for divide & conquer approach for this problem.
# The helper function calculate the maximum possible sum value of
# a provided array, by keeping track of the largest sum possible
# from the middle index.
def middleOutMax(nums, mid_index):

    # Initialize max_sum_left and max_sum_right as negative inf.
    # We can't set these as zero because in a scenario where we
    # get an array that consists entirely of negative values, we'll
    # return incorrect answer.
    max_sum_left = max_sum_right = float('-inf')
    current_sum = 0

    # Loop through the left portion of the array from center,
    # and add each element to current_sum value. If the current_sum
    # exceeds the max_sum_left, we replace it! Otherwise just keep
    # adding onto temporary current_sum value until the end.
    for i in range(mid_index - 1, -1, -1):
        current_sum += nums[i]
        if current_sum > max_sum_left:
            max_sum_left = current_sum

    # reset the current_sum variable:
    current_sum = 0

    # Do the same thing for the right portion of the array:
    for j in range(mid_index, len(nums)):
        current_sum += nums[j]
        if current_sum > max_sum_right:
            max_sum_right = current_sum

    # Below if statements are unnecessary, as adding any integer to
    # zero should still be greater than negative infinity. But they're
    # there as a sanity check...
    if max_sum_left == float('-inf'):
        max_sum_left = 0

    if max_sum_right == float('-inf'):
        max_sum_right = 0

    # return the sum of the left and right array's max sum:
    return max_sum_left + max_sum_right


# Main function:
def maxSubArrDivideAndConquer(nums):

    # Base case: if the length of the array is 1 (or less, but that
    # won't happen), return the lone value of that element:
    if len(nums) <= 1:
        return nums[0]

    mid_index = len(nums) // 2

    # The idea behind divide and conquer algorithm is simple -
    # There are three possible scenarios for determining the max sub array,
    # when we divide the array into two sub-arrays:

    # 1) the max possible sum consists of elements only from LEFT side (ex. [1, 2, -3, -4])
    # 2) the max possible sum consists of elements only from RIGHT side (ex. [-1, -2, 3, 4])
    # 3) the max possible sum consists of elements from BOTH sides (ex. [4, -2, -1, 7])

    # When executing divide and conquer, we use recursion to calculate the max sum for scenario
    # 1 and 2. For scenario 3, we use a helper function to determine the largest possible value
    # when using elements from both sub-arrays!

    left_sum = maxSubArrDivideAndConquer(nums[:mid_index])
    right_sum = maxSubArrDivideAndConquer(nums[mid_index:])
    mid_sum = middleOutMax(nums, mid_index)

    # Return the largest among the three different sums as mentioned above:
    return max(left_sum, right_sum, mid_sum)


# Side-notes and test runs below. Ignore...

# WEIRD EDGE CASE FOUND: For an array length == 3, if we have a negative
# value on either the left corner or the right corner, with remaining two
# having values, we'll get different result depending on where we take our
# midpoint value (HOWEVER inputting mid_index -1 on helper function seems
# to fix the issue...)

# Edge case solved. It was the issue with the indexing on line 18 and line 27
# of helper function (for loop range).
#
# Initial setup was: range(mid_index, -1, -1) for left side, range(mid_index + 1, len(nums))
# for right side, and having mid_sum = middleOutMax(nums, mid_index - 1).
#
# Instead, if you take range(mid_index - 1, -1, -1) for left side, and
# range(mid_index, len(nums)) for right side, setting
# mid_sum = middleOutMax(nums, mid_index) is fine.

# # print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# print(list(range(4, -1, -1)))
# # test_list = [-2,1,-3,4,-1,2,1,-5,4]
# test_list = [2, 0, 3, -2]
# test_list_mid = round(len(test_list)/2)
# print(test_list_mid)
# print(test_list[:test_list_mid])
# print(test_list[test_list_mid:])
# # print(test_list[test_list_mid:])
# # print(test_list[:test_list_mid])
# print(maxSubArrDivideAndConquer(test_list))

print(maxSubArrDivideAndConquer([-3, -2, -1]))
# print(maxSubArrDivideAndConquer([-1, 2, 1]))
# print(maxSubArrDivideAndConquer([1, 2, -1]))
# print(maxSubArrDivideAndConquer([-1, -1, 1, 2, 1]))
