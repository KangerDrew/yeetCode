def rob(nums):

    table = [0] * len(nums)

    table[0] = nums[0]
    table[1] = nums[1]

    for i in range(2, len(table)):
        if i - 1 > 0:
            if nums[i] + table[i - 2] > nums[i] + table[i - 3]:
                table[i] = nums[i] + table[i - 2]
            else:
                table[i] = nums[i] + table[i - 3]

    print(table)
    return table[-1] if table[-1] > table[-2] else table[-2]


print(rob([1, 2, 3, 1]))
