# Similar to the maximum (sum) sub-array problem, except now we're multiplying
# the elements to get the largest possible value. In previous problem, we've
#
def maxProduct(nums):

    final_max = float('-inf')
    current_min, current_max = 1, 1

    for n in nums:

        temp_product = n * current_max
        current_max = max(temp_product, current_min * n, n)
        current_min = min(temp_product, current_min * n, n)

        final_max = max(current_max, final_max)

    return final_max

