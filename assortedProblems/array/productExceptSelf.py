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

    # First value of the returning array would just be
    # the second element of the postfix array:
    sol = [post[1]]

    # loop from index 1 to len - 2:
    for k in range(1, l - 1):
        sol.append(pre[k - 1] * post[k + 1])

    # Last value of the returning array is just the
    # second last element of the prefix array:
    sol.append(pre[-2])

    return sol


# There is a far more efficient way to do the above solution:
def productExceptSelfFaster(nums):

    # Initialize an answer array, populated by 1 for now:
    answer = [1 for i in range(len(nums))]

    # Initialize a variable to keep track of prefix value:
    prefix = 1
    # Loop through to determine the prefix value that needs
    # to be multiplied at index i:
    for i in range(len(nums)):
        answer[i] = prefix
        prefix *= nums[i]

    # Initialize postfix variable:
    post = 1
    # Loop backwards from the end to determine the postfix
    # value that needs to be multiplied:
    for i in range(len(nums) - 1, -1, -1):
        answer[i] *= post
        post *= nums[i]

    # Return answer array:
    return answer


# print(productExceptSelf([1, 2, 3, 4]))
print(productExceptSelfFaster([1, 2, 3, 4]))
print(productExceptSelfPrePost([1, 2, 3, 4]))
