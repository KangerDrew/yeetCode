def canJumpSlow(nums):

    nums_length = len(nums)
    jump_check = [False for i in range(nums_length)]
    jump_check[0] = True

    # Time complexity is O(n^m) where n is the len of nums list,
    # and m is the largest possible value of an element in nums...
    # VERY BAD!
    for index in range(nums_length):

        if jump_check[index]:
            # I tried to iterate from the LARGEST step to slightly
            # increase the speed, but unfortunately our time complexity
            # is still trash...
            for possible_jump in range(nums[index], 0, -1):
                # Return early if we reach the solution
                if index + possible_jump == nums_length - 1:
                    return True
                if index + possible_jump < nums_length:
                    jump_check[index + possible_jump] = True

    return jump_check[-1]


print(canJumpSlow([2, 3, 1, 1, 4]))
print(canJumpSlow([3, 2, 1, 0, 4]))


