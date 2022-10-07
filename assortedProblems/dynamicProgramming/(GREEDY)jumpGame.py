# IGNORE THIS SLOW SOLUTION! COMPLETELY WRONG APPROACH AND EXTREMELY SLOW!!!
# def canJumpSlow(nums):
#     nums_length = len(nums)
#     jump_check = [False for i in range(nums_length)]
#     jump_check[0] = True
#
#     # Time complexity is O(m ^ n) where n is the len of nums list,
#     # and m is the largest possible value of an element in nums...
#     # This is extremely slow!
#     for index in range(nums_length):
#
#         if jump_check[index]:
#             # I tried to iterate from the LARGEST step to slightly
#             # increase the speed, but unfortunately our time complexity
#             # is still trash...
#             for possible_jump in range(nums[index], 0, -1):
#                 # Return early if we reach the solution
#                 if index + possible_jump == nums_length - 1:
#                     return True
#                 if index + possible_jump < nums_length:
#                     jump_check[index + possible_jump] = True
#
#     return jump_check[-1]


# print(canJumpSlow([2, 3, 1, 1, 4]))
# print(canJumpSlow([3, 2, 1, 0, 4]))
# print(canJumpSlow([2, 5, 0, 0]))


# Found an actual "dynamic programming solution" from web:
def jumpGameDyn(nums):
    dp = [False] * len(nums)
    dp[0] = True
    for i in range(1, len(nums)):

        for j in range(min(i - 1, len(nums) - 1), -1, -1):

            if nums[j] >= i - j and dp[j] is True:
                dp[i] = True
                break

    return dp[-1]


# print(False is None)
print(jumpGameDyn([2, 3, 1, 1, 4]))


# My interpretation of dynamic programming approach - O(n^2) time w O(n) memory:
def jumpGameDynII(nums):
    array_len = len(nums)

    # memo array will tell us which index position is "reachable".
    # Set the default values to False, as we will mark them as True/False
    # when we know for certain if they can reach the last index or not.
    memo = [False for stuff in range(array_len)]
    # Set the LAST value of this array to be reachable. This is simply
    # because last index is the target itself:
    memo[-1] = True

    # From here, we loop from the SECOND LAST INDEX of the nums array.
    # We will utilize the memo array by checking to see if any of the
    # indices ahead of the current ones are able to reach the last index.
    # If yes, that means we can break out of the loop early and proceed
    # to checking the next furthest index from the final position:

    for i in range(len(nums) - 2, -1, -1):

        largest_jump = min(array_len - i, nums[i] + 1)
        for jumpVal in range(1, largest_jump):

            if memo[i + jumpVal]:
                memo[i] = True
                break

    return memo[0]


# print(jumpGameDynII([3, 2, 1, 0, 4]))


# Instead of a traditional dynamic programming approach,
# we can use greedy approach to solve this problem:
def canJumpGreedy(nums):
    edge = 0

    for i, num in enumerate(reversed(nums)):
        if i - num <= edge:
            edge = i

    return edge == len(nums) - 1


# print(canJumpGreedy([2, 3, 1, 1, 4]))
# print(canJumpGreedy([3, 2, 1, 0, 4]))


def canJumpGreedyAlt(nums):
    goal = len(nums) - 1

    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= goal:
            goal = i

    return goal == 0
