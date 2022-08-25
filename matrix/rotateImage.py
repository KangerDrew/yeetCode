# The function will not return anything,
# it'll simply mutate the input matrix

# Assume all matrix inputs are square!

def rotate(matrix):

    # Get the left & right bound of the matrix:
    l, r = 0, len(matrix) - 1

    while l < r:
        # We will get values from 0 to r - 1, and rotate the matrix clockwise.
        # See video explanation on youtube for visualization:
        for i in range(r - 1):
            # We are assuming all matrices will be square, so we can
            # get the top and bottom easily:
            top, bottom = l, r

            # First, store the top left element of rotation:
            topLeft = matrix[top][l + i]

            # Move the bottom left into the topLeft position:
            matrix[top][l + i] = matrix[bottom - i][l]

            # Now move the bottom right into bottom left:
            matrix[bottom - i][l] = matrix[bottom][r - i]

            # Then move the top right into the bottom left:
            matrix[bottom][r - i] = matrix[top + i][r]

            # Finally, place the stored topLeft into top right:
            matrix[top + i][r] = topLeft

        # Increment r and l:
        r -= 1
        l += 1

    return None



