# This dynamic problem's worst case scenario is O(2^n), since on each
# step, we can either take a single number, or two numbers (if it is
# between 1 to 26).
def numDecodings(s):

    dp = {len(s): 1}

    # The helper works by taking the index "i" as input,
    def helper(i):
        if i in dp:
            return dp[i]

        # For debugging purpose:
        current = s[i]

        # Edge case: If the first value is zero, there are no
        # ways to decode from that particular solution:
        if s[i] == "0":
            return 0

        # Recursively calculate how much
        res = helper(i + 1)

        #
        if i + 1 < len(s) and (s[i] == "1" or
                               (s[i] == "2" and s[i + 1] in "0123456")):
            res += helper(i + 2)

        dp[i] = res

        return res

    return helper(0)


print(numDecodings("1220"))
