def productExceptSelf(nums):
    answer = []

    for i in range(len(nums)):
        val = 1
        for j, num in enumerate(nums):
            if i is not j:
                val = num * val

        print(val)
        answer.append(val)

    return answer


def productExceptSelfFaster(nums):
    answer = [1]

    for i in range(1, len(nums)):
        answer.append(nums[i - 1] * answer[i - 1])

    post = 1
    for j in range(len(nums) - 1, -1, -1):
        answer[j] *= post
        post *= nums[j]

    return answer


# print(productExceptSelf([1, 2, 3, 4]))
print(productExceptSelfFaster([1, 2, 3, 4]))
