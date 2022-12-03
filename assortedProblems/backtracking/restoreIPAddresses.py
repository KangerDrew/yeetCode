# Hint: If the input is greater than 12 characters in length, it is impossible
# to create a valid IP address from it!


def restore(s):

    res = []

    # Edge case as we discussed:
    if len(s) > 12:
        return res
