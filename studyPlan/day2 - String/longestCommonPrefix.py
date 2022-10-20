# Simple solution, we need to loop through each character in all
# the words and check how many of them match:

def longestCommonPrefix(strs):

    # Initialize empty string we'll add onto once we check the letters match:
    res = ""

    # We need to loop through a string. We can just pick the first string in
    # the strs array. This is okay because of two reasons:
    # 1 - If there are shorter string than strs[0] somewhere in the array, we
    # will have our for loop exit early and return the res.
    # 2 - On the other hand, if the first string is shorter than the other string
    # and we don't break early, that means this string itself is the longest
    # common prefix!
    for i in range(len(strs[0])):

        # Now, loop through rest of the strings, except for the first string which
        # we're using as a comparison:
        for word in strs[1:]:
            # Break conditions - we return here if either conditions are met:
            # 1 - The current word is shorter than strs[0] and i is out of bounds
            # 2 - The letters in the index i does not match
            if len(word) <= i or word[i] != strs[0][i]:
                return res

        # If the inner for loop finished without exiting early, it means letters
        # at index i are common. Add it onto the res:
        res += strs[0][i]

    # Return here if the above nested for loop didn't return early. It means strs[0]
    # is the longest common prefix itself.
    return res
