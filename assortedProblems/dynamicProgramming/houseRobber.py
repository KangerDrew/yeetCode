def rob(nums):

    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return max(nums[0], nums[1])

    # Tabulation: Each element of max_rob array (list) represents the
    # "maximum" sum of the sub-array previous (including) the current element

    max_rob = [0 for i in range(len(nums))]
    max_rob[0] = nums[0]
    max_rob[1] = max(nums[0], nums[1])

    for current_max in range(2, len(nums)):

        # Calculate the current max, which should be the larger of either
        # the current num value + max value 2 indices ago, or
        # the max value 1 index ago.
        max_rob[current_max] = max(max_rob[current_max - 2] + nums[current_max], max_rob[current_max - 1])

    print(max_rob)
    return max_rob[-1]


print(rob([1, 2, 3, 1, 5, 3, 1, 2, 1]))
print(rob([2, 1, 1, 2]))


def improved(nums):
    rob1, rob2 = 0, 0

    for n in nums:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp

    return rob2


print(improved([1, 2, 3, 1, 5, 3, 1, 2, 1]))
print(improved([2, 1, 1, 2]))
