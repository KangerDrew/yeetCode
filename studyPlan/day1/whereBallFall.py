# My first blind attempt at this problem is to use hash set to keep
# track of which slot led to which position at the bottom:

# Update - I just realized dynamic programming approach is slightly
# less efficient, since there are no way for balls starting at different
# position to end up at the same position, UNLESS the ball doesn't end up

# def whereBallFallDyn(grid):
#
#     # Memoization set:
#     travelled = set()
#
#     for c in range(len(grid[0])):
#
#         # Keep track of which column we started:
#         startingPoint = c
#         # Keep track of the trajectory of the ball:
#         trajectory = []
#
#         for r in range(len(grid)):


# Simple "DFS" traversal solution:
# m = row; n = column;
# Time Complexity - O(m * n)
# Space Complexity - O(m), since we enter at most m recursive stack
def whereBallFallDFS(grid):

    def dfs(row, col):
        # Base case where ball reached the bottom:
        if row == len(grid):
            return col

        # nextCol is the column position that ball should end up given
        # the current slant orientation:
        nextCol = col + grid[row][col]

        # 1 - If the column is out of bounds, ball will be stuck.
        # 2 - If the slant at [row][nextCol] does not match, the ball will get stuck.
        if not (0 <= nextCol < len(grid[0])) or grid[row][col] != grid[row][nextCol]:
            return -1

        # If the ball didn't get stuck, proceed downwards:
        return dfs(row + 1, nextCol)

    res = []

    for i in range(len(grid[0])):
        res.append(dfs(0, i))

    return res


# Iterative solution, better than dfs approach since space complexity is
# going to be O(1) because there's no recursion stack:
