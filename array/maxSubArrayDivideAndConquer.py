# Helper function for divide & conquer approach for this problem:
def middleOutMax(nums, mid_index):
    current_sum = 0
    max_sum_left = float('-inf')

    for i in range(mid_index, -1, -1):
        print('here')
        current_sum += nums[i]
        if current_sum > max_sum_left:
            max_sum_left = current_sum

    if max_sum_left == float('-inf'):
        max_sum_left = 0

    current_sum = 0
    max_sum_right = float('-inf')

    for j in range(mid_index + 1, len(nums)):
        print('here right')
        current_sum += nums[j]
        if current_sum > max_sum_right:
            max_sum_right = current_sum

    if max_sum_right == float('-inf'):
        max_sum_right = 0

    return max_sum_left + max_sum_right


#
def maxSubArrDivideAndConquer(nums):

    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]

    mid_index = len(nums) // 2
    left_sum = maxSubArrDivideAndConquer(nums[:mid_index])
    right_sum = maxSubArrDivideAndConquer(nums[mid_index:])
    mid_sum = middleOutMax(nums, mid_index - 1)

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
print(maxSubArrDivideAndConquer([-1, 2, 1]))
print(maxSubArrDivideAndConquer([1, 2, -1]))
print(maxSubArrDivideAndConquer([-1, -1, 1, 2, 1]))
