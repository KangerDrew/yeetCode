def climbingStairs(n):
    if n == 1:
        return 1

    table = [0] * n
    table[0], table[1] = 1, 2

    for i in range(2, n):
        table[i] = table[i - 1] + table[i - 2]

    return table[-1]


def climbingStairsRecursive(stairs, memo=None):
    if memo is None:
        memo = {}

    if stairs in memo:
        return memo[stairs]

    if stairs == 2:
        return 2
    if stairs == 1:
        return 1

    if stairs <= 0:
        return 0

    memo[stairs] = climbingStairsRecursive(stairs - 1, memo) + climbingStairsRecursive(stairs - 2, memo)
    return memo[stairs]
