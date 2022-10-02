# Simple solution, we need to loop through each character in all
# the words and check how many of them match:

def longestCommonPrefix(strs):

    res = ""

    for i in range(len(strs[0])):
        for word in strs:
            if len(word) <= i or word[i] != strs[0][i]:
                return res

        res += strs[0][i]

    return res
