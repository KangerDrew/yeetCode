# This dynamic problem's worst case scenario is O(2^n), since on each
# step, we can either take a single number, or two numbers (if it is
# between 1 to 26).
def numDecodings(s):

    # Initialize a cache, where len(s) gives us the final_index + 1 value.
    # If we reach the very end of the string (final_index + 1), that means
    # we've successfully decoded the string once:
    dp = {len(s): 1}

    # The helper works by taking the index "i" as input,
    def helper(i):
        if i in dp:
            return dp[i]

        # For debugging purpose:
        current = s[i]

        # Edge case: If the current value is zero, there are no
        # ways to decode from that particular solution:
        if s[i] == "0":
            return 0

        # Recursively calculate how many possible ways strings can be decoded
        # from current index + 1
        res = helper(i + 1)

        # Then, we check to see if we are able to take two values at once -
        # first check that the index will not overflow (i + 1 < len(s))
        # Then, we check that first index is either 1 or two, and second
        # index is between 0 and 6:
        if i + 1 < len(s) and (s[i] == "1" or
                               (s[i] == "2" and s[i + 1] in "0123456")):
            # Recursively calculate this alternate solution onto res:
            res += helper(i + 2)

        # Store the result into the dp dictionary:
        dp[i] = res

        # IMPORTANT: Unlike most other dynamic programming, we do not add onto the
        # value of res, but instead simply pass it back to the top as it is!
        return res

    # Return the result from helper function (at 0th index):
    return helper(0)


print(numDecodings("1220"))
