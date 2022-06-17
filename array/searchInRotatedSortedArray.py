# This is a binary search problem, where we take advantage
# of the fact that the provided array was originally sorted,
# but is now rotated by an undisclosed amount:
def search(nums, target):

    # Define the left & right index of the full array:
    left, right = 0, len(nums) - 1

    while left <= right:

        # Find the midpoint of the current boundary:
        # Below mid implementation can lead to overflow
        # for some languages:
        # mid = (right + left) // 2

        # This is a better way to implement mid value:
        mid = left + (right - left) // 2

        # If match is found at mid, return the index:
        if nums[mid] == target:
            return mid

        # Otherwise, there are four possible scenarios:


    return -1
