# This is a variant of a popular problem two sums, except the given
# array is sorted...

# Sorted array indicates the use of two pointers (not binary search)!
# One pointer will begin at the beginning of array, another will begin
# at the end of the array.

# We increment the beginning pointer if the two sum is too small, and
# we increment the end pointer if the two sum is too large!

# Add +1 to the index value when returning... Not sure why...

def twoSumsII(numbers, target):

    # Initialize two pointers
    start, end = 0, len(numbers) - 1

    # Use while loop to increment the pointers:
    while end > start:

        current_sum = numbers[end] + numbers[start]

        if current_sum == target:
            return [start + 1, end + 1]
        elif current_sum > target:
            end -= 1
        else:
            start += 1

    # We don't need a return statement, since it was given that
    # we will have ONE solution.
