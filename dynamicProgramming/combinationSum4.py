def combinationSum4(nums, target):

    combo_list = [0 for i in range(target + 1)]
    combo_list[0] = 1

    for current_number in range(1, target + 1):

        for num in nums:
            if combo_list[current_number - 1] != 0 and current_number + num <= target + 1:

                combo_list[current_number + num - 1] += combo_list[current_number - 1]

    return combo_list[-1]


# print(combinationSum4([1, 2, 3], 4))
# print(combinationSum4([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], 10))


def improved(nums, target):
    dp = {0: 1}

    for total in range(1, target + 1):
        dp[total] = 0
        for n in nums:
            dp[total] += dp.get(total - n, 0)

    return dp[target]


print(improved([1, 2, 3], 4))
print(improved([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], 10))


def combinationSum4Dict(nums, target):

    combo_list = {i: 0 for i in range(target + 1)}
    combo_list[0] = 1

    for current_number in range(1, target + 1):

        for num in nums:
            if combo_list[current_number - 1] != 0 and current_number + num <= target + 1:

                combo_list[current_number + num - 1] += combo_list[current_number - 1]

    return combo_list[target]


print(combinationSum4Dict([1, 2, 3], 4))
print(combinationSum4Dict([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], 10))
