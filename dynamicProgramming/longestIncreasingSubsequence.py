def lengthOfLIS(nums):
    # From solution, this is slightly faster O(n^2) solution.
    # This solution works because we do not need to return the exact
    # subsequence, but only the length!

    # The reason why this works is because we increase the length of the
    # sub list, when a newest largest value is introduced. Otherwise, we
    # replace the value within the sub with a new one instead. This doesn't
    # affect the length of the sub list, but it makes it so that the newly
    # edited sub list will still maintain the temporal order of the nums list.

    # Example: [8, 1, 6, 2, 3, 10]  # (see approach 2)
    # When we get to analyzing 2 (index 3) as our num, our sub list will be [1, 6].
    # Since 2 is larger than 1 but smaller than the greatest (last) value of the sub
    # list, the new sub list becomes [1, 2]. Notice that this new sub list changed
    # its greatest value, thus allowing us to build it further in the following
    # for loop iteration!

    # Although this function returns the correct length, it does NOT return
    # the correct sub list. This happens when we start replacing the middle
    # values of our sub list (i.e length doesn't change but middle values
    # get tampered, resulting in non-valid sub list), instead of replacing the
    # largest value of sub list.

    # Another example - [3, 4, 5, 1] will return the sub array of [1, 4, 5], even
    # though such subarray does not exist in the original input. This happens
    # because by the time we assess 1 (index 3), we're at a situation where we
    # need to replace 1 into the sub, and 3 is the first value greater than or
    # equal to 1.
    # THE IMPORTANT THING is that the length of the sub is maintained, and if original
    # array had additional values, the if statement will compare the following value
    # with the last and largest value of sub array to see if we can append & increase
    # the length of the sub array!

    sub = [nums[0]]

    for num in nums[1:]:
        if num > sub[-1]:
            sub.append(num)
        else:
            # Find the first element in sub that is
            # greater than or equal to num

            # Do a linear scan to see which value is greater than
            # or equal to num. However, we can use binary search
            # instead to make this portion of the code run faster
            # i.e. O(n) * O(log n) instead of O(n) * O(n)

            i = 0

            # Note: while loop will simply break if sub[i] is
            # out of bounds... Weird...
            while num > sub[i]:
                i += 1
            sub[i] = num

    return len(sub)


print(lengthOfLIS([4, 2, 1, 4, 3, 7]))
print(lengthOfLIS([8, 1, 6, 2, 3, 10]))
print(lengthOfLIS([3, 2, 1]))
print(lengthOfLIS([1, 2, 3]))



def lengthOfLISBinarySearch(nums):

    def binarySearch(arr, target):
        left = 0
        right = len(arr) - 1

        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid

            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid

        # At this point after while loop, right and left
        # pointers have the exact same value:
        return left

    sub = [nums[0]]

    for num in nums[1:]:
        if num > sub[-1]:
            sub.append(num)
        else:
            # Find the first element in sub that is
            # greater than or equal to num

            # Binary search:
            i = binarySearch(sub, num)
            sub[i] = num

    return len(sub)
