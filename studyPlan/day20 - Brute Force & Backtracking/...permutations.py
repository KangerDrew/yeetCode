import collections

# arr = [1, 2, 3]
# new_arr = collections.deque(arr)
# print(new_arr)
# print(len(new_arr))
# new_arr.popleft()
# new_arr.popleft()
# print(len(new_arr))

# test_arr = [1, 2, 3]
# val = test_arr[0]
# val = 4
#
# print(val)
# print(test_arr)


# Idea is to write a function that will return all possible permutations of a given
# input array.

# The approach here is to think about how we can make the problem smaller. If our input
# is [1, 2, 3], how can we make this problem smaller? Start by selecting one of the values

# Let's take the first element 1. What are the possible permutations, if we restrict the first
# value of our permutation to be 1? (i.e. [1, _, _])

# The two following values will form permutations using the sub-array [2, 3]. The order of these
# two values does not necessarily matter...

# If our function can return all possible permutation of a given numbers in array, we can simply
# append those combinations onto 1.

# Then, we just repeat the process for 2 and 3 as well. We can do this by appending 1 back to the
# end of the array [1, 2, 3] => [2, 3, 1], where after we will remove the first element (converting
# the array to deque and using .popleft() would make this process faster...) and use the remaining
# [3, 1] sub-array to recursively obtain all possible permutation using those two numbers only...
# and continue until we've done this process for all elements in the original array!

def permutations(nums):

    # Convert the input array so we can use .popleft() operation at O(1) time complexity:
    new_nums = collections.deque(nums)

    def get_perms(arr):

        # Base case - Only 1 number in the nums array, so only 1 possible permutation.
        # Return that number, as a nums deque in a deque:
        if len(arr) == 1:
            return collections.deque([collections.deque([arr[0]])])

        # Otherwise, we need to go into recursive stack to return all possible permutations:
        res = collections.deque()

        # Loop through all the elements in the deque (arr):
        for i in range(len(arr)):

            # Remove the current first element:
            current = arr.popleft()

            # Recursively get all possible permutations using the remaining elements:
            sub_perms = get_perms(arr)

            # With our newly obtained sub_perms, we loop through and append all the new
            # permutations that we get by adding the "current" value at the beginning

            for perm in sub_perms:
                perm.appendleft(current)
                res.append(perm)

            # We've added all possible permutations that could occur, if we fix the current
            # value as the first permutation value! Append the current value at the end
            # of the deque (arr) and repeat the process until we've done the same for all
            # values in the input:
            arr.append(current)

        # Return the newly obtained permutations:
        return res

    return get_perms(new_nums)
