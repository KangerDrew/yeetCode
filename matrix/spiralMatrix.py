# The idea is to use multiple for loops for traveling in a
# spiral motion around the matrix.

# We will also define boundaries to determine where we'll be
# starting our for loops from - where the boundary values will
# increase/decrease as we travel in spiral around the matrix:
def spiralOrder(matrix):
    # Get the boundary of the matrix
    b_left, b_right = 0, len(matrix[0])
    b_top, b_bottom = 0, len(matrix)
    spiral = []

    while b_left < b_right and b_top < b_bottom:

        # First, travel the top row from left to right:
        for i in range(b_left, b_right):
            spiral.append(matrix[b_top][i])

        # Top row is successfully appended, increment top boundary by +1
        b_top += 1

        # Second, travel the right column from top to bottom:
        for i in range(b_top, b_bottom):
            spiral.append(matrix[i][b_right - 1])

        # Right column is successfully appended, increment right boundary by -1
        b_right -= 1

        # At this point, if we're using the boundary check to persist while loop,
        # we need an if statement to check if our boundaries have been crossed:
        if not (b_left < b_right and b_top < b_bottom):
            break

        # Third, travel the bottom row from right to left.
        # Beware how to set the boundaries, as we need to NOT
        # include the rightmost value (out of bounds). Also, in
        # python, the second input of range is not inclusive so
        # we need to consider that as well. The third input is the
        # step, which should be -1:
        for i in range(b_right - 1, b_left - 1, - 1):
            spiral.append(matrix[b_bottom - 1][i])

        # Bottom row is successfully appended, increment bottom boundary by -1
        b_bottom -= 1

        # Finally, travel the left column from bottom to top.
        # Setup boundary in similar fashion as previous traversal...
        for i in range(b_bottom - 1, b_top - 1, -1):
            spiral.append(matrix[i][b_left])

        # Left column is successfully appended, increment left boundary by +1
        b_left += 1

    return spiral


print(spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
