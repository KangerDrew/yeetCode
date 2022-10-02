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

