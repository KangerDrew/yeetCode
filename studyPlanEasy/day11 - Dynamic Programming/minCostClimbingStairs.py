# new dp problem

# Sorta reminiscent of the jump game problem, where we divide the questions into
# smaller pieces to solve them.


def minCost(cost):

    memo = [0 for i in range(len(cost) + 1)]
    memo[-2] = cost[-1]

    for i in range(len(memo) - 3, -1, -1):
        memo[i] = min(cost[i] + memo[i + 1], cost[i] + memo[i + 2])

    return min(memo[0], memo[1])
