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


def combinationSum(candidates, target):

    res = []
    cand_count = len(candidates)

    def dfs(i, cur, total):

        if total == target:
            res.append(cur.copy())
            return
        if i >= cand_count or total > target:
            return

        # Scenario 1: We want to continue using current candidate in
        # our combination:
        # Append the current candidate in our potential combination:
        cur.append(candidates[i])
        # Traverse down the decision, after incrementing total:
        dfs(i, cur, total + candidates[i])
        # After the above recursion stack is removed, clean up and
        # remove the candidate that was just added in this current
        # stack, which should be the last one in the cur array:
        cur.pop()

        # Scenario 2: We don't want to include the current candidate
        # any more in our combination. Increment i and continue:
        dfs(i + 1, cur, total)

        # NOTE: Scenario 1 and 2 can be interchanged!!

    # Execute recursive function from the beginning:
    dfs(0, [], 0)
    # Return the obtained result:
    return res


print(combinationSum([2, 3, 6, 7], 7))
