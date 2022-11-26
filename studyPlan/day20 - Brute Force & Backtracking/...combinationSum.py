# This might seem like a generic dynamic programming problem, but unfortunately the most
# ideal approach is the brute force backtracking method.

# We must return all possible combinations, NOT permutations (i.e. our answer cannot return
# the exact same candidate groups with differing orders
# WRONG: [[2, 2, 3], [2, 3, 2], [3, 2, 2], [7]]
# CORRECT: [[2, 2, 3], [7]]

# To prevent combinations with identical permutations from being recorded, we use a specific
# backtracking method. At the beginning, we mark the first element with an index in the candidate
# array to be used in our possible combination.
# Then, we ask ourselves, do we continue to incorporate this same candidate in assembling our
# combination? If we do include it, we increment the total value by that element, add that element
# to the possible combination, and continue down the decision tree.
# If we decide not to use the value, we increment the index (signifying we're no longer using any
# elements before that index), and continue down THAT path instead.



