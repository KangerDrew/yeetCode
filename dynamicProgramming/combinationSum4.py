def combinationSum4(nums, target):

    combo_list = [0 for i in range(target + 1)]
    combo_list[0] = 1

    for current_number in range(1, target + 1):

        for num in nums:
            if combo_list[current_number - 1] != 0 and current_number + num <= target + 1:

                combo_list[current_number + num - 1] += combo_list[current_number - 1]

    return combo_list[-1]


print(combinationSum4([1, 2, 3], 4))
print(combinationSum4([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25], 10))
