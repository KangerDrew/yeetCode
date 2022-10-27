# My first attempt:

def isSubsequence(s, t):

    s_pointer = 0

    for t_string in t:

        if s_pointer == len(s):
            break

        if s[s_pointer] == t_string:
            s_pointer += 1

    return s_pointer == len(s)
