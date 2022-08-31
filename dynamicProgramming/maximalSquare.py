# The idea behind solving this problem is to use memoization (cache) to
# track the largest square length at a given position. For my implementation,
# I will calculate the largest squares from top left to bottom right (TLBR).
# (how it's done in leetcode solution, but not how it's done in neetcode vid)

# If we do TLBR, the rightmost column and topmost row's largest square value
# will simply be either be 0 or 1. (can't check beyond it). From there, we iterate
# from 1, 1 position, and see what the previous top, previous left, and previous
# topleft largest square value was. The minimum between these values, and the
# current value (whether it's 1 or 0) will determine the largest possible square
# length at that given position, when excluding the remaining matrix at the bottom.

# See solution on leetcode or video for better visualization explanation...

def maximalSquare(matrix):
    rows, columns = len(matrix), len(matrix[0])
    memo = [[0 for i in range(columns)] for j in range(rows)]
    currentMaxLen = 0

    for r in range(rows):
        for c in range(columns):

            # The largest square at a given position cannot be greater than zero
            # if the value is not "1" in the matrix. Check if the value is "1":
            if matrix[r][c] == "1":
                memo[r][c] = 1

                # Extra safeguard to make sure we only use memoization for positions that
                # are NOT leftmost and topmost:
                if r > 0 and c > 0:
                    memo[r][c] += min(memo[r - 1][c], memo[r][c - 1], memo[r - 1][c - 1])

                # Update the current max length:
                currentMaxLen = max(currentMaxLen, memo[r][c])

    # return the largest possible square area:
    return currentMaxLen * currentMaxLen


# print(maximalSquare(
#     [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
# print(maximalSquare([["0", "1"], ["1", "0"]]))
print(maximalSquare([["1", "0", "1", "1", "0", "1"],
                     ["1", "1", "1", "1", "1", "1"],
                     ["0", "1", "1", "0", "1", "1"],
                     ["1", "1", "1", "0", "1", "0"],
                     ["0", "1", "1", "1", "1", "1"],
                     ["1", "1", "0", "1", "1", "1"]
                     ]))
