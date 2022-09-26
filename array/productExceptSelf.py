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


# The simplest solution that runs at O(n) without the use of division
# requires a use of two arrays - one containing all the multiples
# prior to the index (prefix) and another containing the multiples
# after the index (postfix).

# Ex. [1, 2, 3, 4]

# Prefix:   [1, 1*2, 1*2*3, 1*2*3*4]
#            ======================>
# Postfix:  [4*3*2*1, 4*3*2, 4*3, 4]
#            <======================

# For a given index i, if we want to get the


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
