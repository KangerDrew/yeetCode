

def backspaceCompare(s, t):

    # We will assess our letters from ENDING, not from beginning.
    # This will allow us to handle backspace without needing a O(n)
    # storage:
    s_pointer, t_pointer = len(s) - 1, len(t) - 1
    # We need variable to store how many times we must skip because
    # of backspace:
    s_skip, t_skip = 0, 0

    while s_pointer >= 0 or t_pointer >= 0:

        # First, remove letters from backspace:
        while s_pointer >= 0:
            # If the current string is backspace, decrement pointer,
            # and add +1 to the skip value.
            if s[s_pointer] == '#':
                s_skip += 1
                s_pointer -= 1
            # ELSE IF, the skip value is greater than 0, we decrement
            # both skip and pointer counter:
            elif s_skip > 0:
                s_skip -= 1
                s_pointer -= 1
            # If none above is true, we break out of this while loop:
            else:
                break

        # Same process as above:
        while t_pointer >= 0:
            if t[t_pointer] == '#':
                t_skip += 1
                t_pointer -= 1
            elif t_skip > 0:
                t_skip -= 1
                t_pointer -= 1
            else:
                break

        # Note: If the pointer value has reached negative, it means
        # that there is nothing left to compare. From here there are two
        # questions to consider:

        # 1) Did one of the pointer reach negative before the other? If yes that means
        # two strings are not equivalent as one will result in more characters:

        # In other words - If expecting to compare char vs nothing:
        if (s_pointer >= 0) != (t_pointer >= 0):
            return False

        # 2) First, check that both pointers are positive. If so, confirm that those two
        # characters at the pointer are equal:

        # In other words - If two actual characters are different:
        if s_pointer >= 0 and t_pointer >= 0 and (s[s_pointer] != t[t_pointer]):
            return False

        # Decrement after checking above:
        s_pointer -= 1
        t_pointer -= 1

    return True