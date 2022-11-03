# Going to try to solve this problem recursively...


def climbStairs(n):

    memo = {}

    def climbRecur(n):
        if n in memo:
            return memo[n]
        if n == 1:
            return 1
        if n == 2:
            return 2

        memo[n] = climbRecur(n - 1) + climbRecur(n - 2)
        return memo[n]

    return climbRecur(n)
