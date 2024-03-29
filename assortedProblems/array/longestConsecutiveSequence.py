def bruteForceSequence(nums):
    output_max = 0
    # Linear time for looping through nums:
    for num in nums:
        temp_max = 1

        # Since we're looking through an array, we
        while num + 1 in nums:
            temp_max += 1
            num += 1

        output_max = max(temp_max, output_max)

    return output_max


print(bruteForceSequence([100, 4, 200, 1, 3, 2]))
print(bruteForceSequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))


def findSequenceUsingSort(nums):
    # Return 0 if array is empty:
    if not nums:
        return 0

    # Sort the array:
    nums.sort()

    # Create two variables, one for tracking temporary max length,
    # another for tracking overall max length
    current_sequence = 1
    largest_sequence = 0

    for i in range(len(nums) - 1):
        # If there is a repeated value within the array,
        # we need to skip the loop until the next value
        # is different:
        if nums[i] != nums[i + 1]:
            # Check if the next value is greater by 1:
            if nums[i + 1] == nums[i] + 1:
                current_sequence += 1
            # If not, that means current_sequence is at max. Thus
            # compare it with the largest_sequence, and take the
            # largest between the two
            else:
                largest_sequence = max(largest_sequence, current_sequence)
                # reset temporary value current_sequence:
                current_sequence = 1

    # We need to use max() function to compare largest_sequence and current_sequence,
    # in case the largest sequence occurred at the end of the sorted array and max()
    # was not executed:
    return max(largest_sequence, current_sequence)


print(findSequenceUsingSort([100, 4, 200, 1, 3, 2]))
print(findSequenceUsingSort([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))


def longestSequence(nums):

    # Convert the nums to sets for constant access.
    # python should automatically get rid of repeating
    # values (e.x. [1, 2, 1, 1, 3] ==>  {1, 2, 3}):
    numSet = set(nums)

    output_max = 0

    # Loop through each value in numSet:
    for n in numSet:
        # if n - 1 is not in numSet, that means
        # n is the beginning of a sequence:
        if n - 1 not in numSet:

            # Set a temporary max:
            temp_max = 1

            # Use while loop to check continuously if
            # next value in the sequence exist, and increment
            # temp_max value by 1 if so and continue:

            # The reason why below while loop doesn't make this
            # O(n^2) solution is because that the while loop will
            # only run when we are at the beginning of a sequence.
            # Furthermore, while loop will at most run for the
            # length of the nums array (less if there are repeating
            # numbers) since all the while loop does is it iterates
            # to the +1 value IF it exists.

            while n + 1 in numSet:
                temp_max += 1
                n += 1

            # compare temp_max to the old output_max value:
            output_max = max(output_max, temp_max)

    # Return the output_max
    return output_max


print(longestSequence([100, 4, 200, 1, 3, 2]))
print(longestSequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))