# The 3sum problem can be broken down into multiple two sum II problems.
# But first, we sort the input array!


# There will be three pointers in this problem - start, left, and right.

# Starting Pointer - The pointer that determines the first value we use to
# check for possible 3 sum combo.
# Left Pointer - This pointer is the "start" pointer from two sums II problem
# Right Pointer - This is the "end" pointer

# Once we select the start pointer, we use the remaining values to the right
# to conduct a two sum II problem, where the two sum value must be the "opposite
# number" to that of the one in the starting pointer!

# NOTE - if value at the start pointer reaches/exceeds 0, that means we can finish
# looking for possible combo since all the values remaining for testing will
# always return sum greater than zero!


def threeSum(nums):

    all_sums = []
    # Use .sort() function:
    nums.sort()


    # Begin looping from the start of the sorted list:
    for start, start_val in enumerate(nums):

        # As mentioned earlier, if the start pointer reaches/exceeds 0,
        # it means there are no possible combinations left:
        if start_val >= 0:
            break

        # Furthermore, we need to check that the current value is NOT
        # the duplicate of previous value. We first confirm that the "start"
        # index is greater than 0 (i.e. we're not at the beginning of nums,
        # so that we're not going out of bounds), and that start_val equals
        # previous val. If so, skip the current loop!:
        if start > 0 and start_val == nums[start - 1]:
            continue




