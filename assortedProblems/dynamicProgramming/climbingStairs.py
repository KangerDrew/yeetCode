def climbingStairs(n):
    if n == 1:
        return 1

    table = [0] * n
    table[0], table[1] = 1, 2

    for i in range(2, n):
        table[i] = table[i - 1] + table[i - 2]

    return table[-1]


print(climbingStairs(6))


def climbingStairsRecursive(n):
    if n <= 1:
        return 1

    return climbingStairsRecursive(n - 1) + climbingStairsRecursive(n - 2)


print(climbingStairsRecursive(6))
