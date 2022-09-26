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

# For a given index i, if the product except self at i in nums is:
# prefix[i - 1] * postfix[i + 1]

# If prefix/postfix is out of bounds (i.e. at index 0 or at the end
# of the list), we take 1 as our out of bounds prefix/postfix value
# and multiply by our non-out of bounds prefix/postfix.

def productExceptSelfPrePost(nums):

    l = len(nums)
    pre = [nums[0]]
    post = [nums[-1]]

    for i in range(1, l):
        pre.append(pre[i - 1] * nums[i])

    for j in range(l - 2, -1, -1):
        post.insert(0, nums[j] * post[0])

    print("pre array")
    print(pre)
    print("post array")
    print(post)

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
print(productExceptSelfPrePost([1, 2, 3, 4]))
