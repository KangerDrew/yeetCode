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


        valLeft = nums[left]
        valMid = nums[mid]
        valRight = nums[right]

        # If match is found at mid, return the index:
        if nums[mid] == target:
            return mid

        # We need to determine where the inflection point occurs:
        # The inflection point is where the smallest value of the sorted
        # array is. For a section that doesn't have the inflection point,
        # we can treat it like a regular non-rotated sorted array and see
        # if the range of the sub-list can contain the target value. If yes,
        # we adjust the left/right boundary to analyze that sub-section.
        # Otherwise, it means that we need to check other sub-section with
        # inflection point to see if it contains the target value.

        # We can find the side without the inflection point by checking the
        # mid value against left/right boundaries. The side without the

        # DO NOT FORGET EQUAL SIGNS!!
        # Check #1a: Inflection point is located at the left side:
        if nums[mid] >= nums[left]:
            # Check #2a: The target value lies in the range of left sub-section:
            if nums[mid] >= target >= nums[left]:
                # Change right value so we'll analyze left sub-section:
                right = mid - 1
            # If not, that means we need to check the right section with inflection
            # to see if it contains the target value:
            else:
                # Change left value so we'll analyze right sub-section:
                left = mid + 1
        # Check #1b: The inflection point is at the right side (can also
        # use "if nums[right] > nums[mid]):
        else:
            # Check #2b: The target value lies in the range of right sub-section:
            if nums[right] >= target >= nums[mid]:
                # Change left value so we'll analyze right sub-section:
                left = mid + 1
            # If not, that means we need to check the left:
            else:
                # Change left value so we'll analyze right sub-section:
                right = mid - 1

    return -1


print(search([4, 5, 6, 7, 0, 1, 2], 0))
