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

        # Use for loop to iterate 3 letters forward, OR until we reach the end of the string:
        for j in range(i, min(i + 3, s_len)):

            # Check 1 - Is the string we've scanned below the value of 256?
            # Check 2 - Did we select more than one letters? If we have more than 1 letters,
            # we need to make sure there are no leading zeros!
            if int(s[i:j+1]) < 256 and (i == j or s[i] != "0"):

                # Recursively call the helper again, this time incrementing i forward by
                # the current j value, adding onto the current_ip, and incrementing p_count:
                backtrack(j + 1, current_ip + s[i:j+1] + ".", p_count + 1)

    # Execute backtrack helper:
    backtrack(0, "", 0)
    # The res list should be populated with all valid IP addresses:
    return res

