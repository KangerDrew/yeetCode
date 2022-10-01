# Two pointers problem. Take two pointers, calculate the distance between
# them (width), and the minimum height between the two, multiply to get the
# area. Increment the pointer with lower height towards the center and continue
# calculating the maximum area. Exit out until the two pointers clash and
# return the largest area recorded.

def containsMostWater(height):

    max_area = 0
    left, right = 0, len(height) - 1

    while left < right:

        current_area = (right - left) * min(height[left], height[right])
        max_area = max(current_area, max_area)

        if height[left] > height[right]:
            right -= 1
        else:
            left += 1

    return max_area
