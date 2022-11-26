# This might seem like a generic dynamic programming problem, but unfortunately the most
# ideal approach is the brute force backtracking method.

# We must return all possible combinations, NOT permutations (i.e. our answer cannot return
# the exact same candidate groups with differing orders
# WRONG: [[2, 2, 3], [2, 3, 2], [3, 2, 2], [7]]
# CORRECT: [[2, 2, 3], [7]]

# To prevent combinations with identical permutations from being recorded, we traverse down
# the decision tree as...
