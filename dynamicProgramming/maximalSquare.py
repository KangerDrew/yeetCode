# The idea behind solving this problem is to use memoization (cache) to
# track the largest square length at a given position. For my implementation,
# I will calculate the largest squares from top left to bottom right (TLBR).
# (how it's done in leetcode solution, but not how it's done in neetcode vid)

# If we do TLBR, the rightmost column and topmost row's largest square value
# will simply be either be 0 or 1. (can't check beyond it). From there, we iterate
# from 1, 1 position, and see what the previous top, previous left, and previous
# topleft largest square value was. The minimum between these values, and the
# current value (whether it's 1 or 0) will determine the largest possible square
# length at that given position, when excluding the remaining matrix at the bottom

