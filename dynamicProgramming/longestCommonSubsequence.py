def common(text1, text2):
    # Create a matrix that has +1 row & column value as text1 and text2

    # BAD WAY TO CREATE MATRIX, IT CAUSES REFERENCE ISSUE:
    # common_matrix = [[0] * (len(text1) + 1)] * (len(text2) + 1)

    # Right way, using list comprehension:
    common_matrix = [[0 for n in range(len(text1) + 1)] for m in range(len(text2) + 1)]

    # We iterate through each letter of words, where row represent a
    # letter in text2, column represent a letter in text1. Extra column &
    # row at the beginning accounts for an "empty string"

    # See back to back swe video for visual illustration!

    for row in range(1, (len(text2) + 1)):

        for column in range(1, (len(text1) + 1)):
            # If the letters match, that means the solution for this current sub-string
            # is 1 + "best solution, after current letter is removed"
            if text1[column - 1] == text2[row - 1]:
                common_matrix[row][column] = common_matrix[row - 1][column - 1] + 1
            else:
                common_matrix[row][column] = max(common_matrix[row - 1][column], common_matrix[row][column - 1])

    return common_matrix[-1][-1]


# See why we shouldn't use bad way to create matrix (debug @ if statement):
print(common("bsbininm", "jmjkbkjkv"))


# common_matrix = [[0] * (len(text1) + 1)]
# common_matrix = [[0 for n in range(len(text1) + 1)] for m in range(len(text2) + 1)]

something = "abc"
safer = "abc"

print(id(something))
print(id(safer))
