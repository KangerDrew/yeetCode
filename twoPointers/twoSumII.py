# This is a variant of a popular problem two sums, except the given
# array is sorted...

# Sorted array indicates the use of two pointers (not binary search)!
# One pointer will begin at the beginning of array, another will begin
# at the end of the array.

# We increment the beginning pointer if the two sum is too small, and
# we increment the end pointer if the two sum is too large!

# Add +1 to the index value when returning... Not sure why...

def twoSumsII(numbers):
