# Helper function for divide & conquer approach for this problem.
# The helper function calculate the maximum possible sum value of
# a provided array,
def middleOutMax(nums, mid_index):
    current_sum = 0
    max_sum_left = float('-inf')

    for i in range(mid_index - 1, -1, -1):
        current_sum += nums[i]
        if current_sum > max_sum_left:
            max_sum_left = current_sum

    if max_sum_left == float('-inf'):
        max_sum_left = 0

    current_sum = 0
    max_sum_right = float('-inf')

    for j in range(mid_index, len(nums)):
        current_sum += nums[j]
        if current_sum > max_sum_right:
            max_sum_right = current_sum

    if max_sum_right == float('-inf'):
        max_sum_right = 0

    return max_sum_left + max_sum_right


# Main function:
def maxSubArrDivideAndConquer(nums):

    if len(nums) <= 1:
        return nums[0]

    mid_index = len(nums) // 2
    left_sum = maxSubArrDivideAndConquer(nums[:mid_index])
    right_sum = maxSubArrDivideAndConquer(nums[mid_index:])
    # Taking mid_index - 1 as a midpoint seems to address the
    # issue with len = 3 arrays (specifically [1, 2, -1]) that
    # makes this algorithm calculate incorrect sum...
    mid_sum = middleOutMax(nums, mid_index)

    return max(left_sum, right_sum, mid_sum)


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


# WEIRD EDGE CASE FOUND: For an array length == 3, if we have a negative
# value on either the left corner or the right corner, with remaining two
# having values, we'll get different result depending on where we take our
# midpoint value (HOWEVER inputting mid_index -1 on helper function seems
# to fix the issue...)

# Edge case solved. It was the issue with the indexing on line 6 and line 17
# of helper function (for loop range).
#
# Initial setup was: range(mid_index, -1, -1) for left side, range(mid_index + 1, len(nums))
# for right side, and having mid_sum = middleOutMax(nums, mid_index - 1).
#
# Instead, if you take range(mid_index - 1, -1, -1) for left side, and
# range(mid_index, len(nums)) for right side, setting
# mid_sum = middleOutMax(nums, mid_index) is fine.

print(maxSubArrDivideAndConquer([-1, 2, 1]))
print(maxSubArrDivideAndConquer([1, 2, -1]))
print(maxSubArrDivideAndConquer([-1, -1, 1, 2, 1]))
