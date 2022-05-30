def lengthOfLIS(nums):
    sub = [nums[0]]

    for num in nums[1:]:
        if num > sub[-1]:
            sub.append(num)
        else:

            i = 0
            while i < len(sub) and num > sub[i]:
                i += 1

            sub[i] = num

    return len(sub)


print(lengthOfLIS([4, 2, 1, 4, 3, 7]))
print(lengthOfLIS([8, 1, 6, 2, 3, 10]))
print(lengthOfLIS([3, 2, 1]))
print(lengthOfLIS([1, 2, 3]))



