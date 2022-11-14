# Much simpler than it looks

def findIndex(haystack, needle):

    if len(needle) > len(haystack):
        return -1

    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:(i + len(needle))] == needle:
            return i

    return -1
