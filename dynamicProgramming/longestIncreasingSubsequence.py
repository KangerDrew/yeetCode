def lengthOfLIS(nums):
    sub = [nums[0]]

    for num in nums[1:]:
        if num > sub[-1]:
            sub.append(num)
        else:

            i = 0
            while num > sub[i]:
                i += 1

            sub[i] = num

    return len(sub)


print(lengthOfLIS([4, 2, 1, 4, 3, 7]))
print(lengthOfLIS([8, 1, 6, 2, 3, 10]))

val = 4
some_list = [1, 2, 3]
i = 5
if val > some_list[i]:
    i += 1
    print(i)

