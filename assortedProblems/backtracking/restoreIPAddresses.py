# Hint: If the input is greater than 12 characters in length, it is impossible
# to create a valid IP address from it!


def restore(s):

    res = []
    s_len = len(s)
    # Edge case as we discussed:
    if s_len > 12:
        return res

    # Use recursive helper that will branch out to get all possible IP addresses:
    def backtrack(i, current_ip, p_count):

        # Valid Solution - If we reached the end of the string AND have used the required
        # number of periods, we've found a valid IP address:
        if p_count == 4 and i == s_len:
            # Remember to exclude the very last letter, as it would contain an unwanted ".":
            res.append(current_ip[:-1])
            return None

        # Exit Condition - if we reach p_count that's greater than 3, we need to exit
        # out of recursion:
        if p_count > 3:
            return None

        for j in range(i, min(i + 3, s_len)):
            if int(s[i:j+1]) < 256 and (i == j or s[i] != "0"):
                backtrack(j + 1, current_ip + s[i:j+1] + ".", p_count + 1)

    backtrack(0, "", 0)
    return res

