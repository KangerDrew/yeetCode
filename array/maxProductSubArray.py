# Similar to the maximum (sum) sub-array problem, except now we're multiplying
# the elements to get the largest possible value.

# In previous variant problem, we've used the sliding window technique to change
# the left/right boundary of the sub array. The second current_max & current_min
# calculation does something similar to this, where boundary gets adjusted.

# Instead, we will ALSO keep track of the lowest possible minimum value. If there
# are more than one negative values within the array, we can compare the product
# of the lowest possible value (negative) to that of the negative element to see
# if it yields in even greater positive value (ex. [-1, 1, -6])

# Main thing to remember:
# Each time we multiply by a new integer, the quantity (absolute value) will always go up.
# We keep track of both the largest and the lowest value, in case the negative value causes
# them to "flip", and we need to check if it yields a larger quantity!

def maxProduct(nums):

    # Setup variables:
    final_max = float('-inf')
    current_min, current_max = 1, 1

    for n in nums:

        # # The if statement below was to handle the edge case if there
        # # was a zero in the middle of the array, to skip over and reset.
        # # BUT, this will actually cause the function to return an incorrect
        # # answer for this edge case - [-2,0,-1]
        # # This is because skipping the 0 will cause it to return -1, but instead
        # # it should return 0 which is a correct answer:
        # if n == 0:
        #     current_min, current_max = 1, 1
        #     continue

        # Step 1: Calculate the temp_max_product, (n * current_max), and
        # compare that against the temp_min_product. As mentioned before,
        # we keep track of both current_max and current_min in case the
        # n value yields a larger absolute value from one or the other!
        temp_max_product = n * current_max
        temp_min_product = n * current_min
        current_max = max(temp_max_product, temp_min_product)  # NOT THE SAME AS max(n * current_max, current_min * n)
        current_min = min(temp_max_product, temp_min_product)

        # Step 2: Do we re-set the current_max or current_min value?
        # This can happen if the previous element was zero and led to
        # current_max and current_min value to become zero.

        # We also need to do this if the previous negative value caused either the
        # current_max/current_min to become smaller/larger than the n value
        current_max = max(current_max, n)
        current_min = min(current_min, n)

        # compare current_max against final_max:
        final_max = max(current_max, final_max)

    return final_max


print(maxProduct([3, -3, 1, 12, 1]))
