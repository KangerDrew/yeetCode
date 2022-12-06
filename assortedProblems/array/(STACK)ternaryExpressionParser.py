# Statement: Given a string expression representing arbitrarily nested ternary expressions,
# evaluate the expression, and return the result of it.

# You can always assume that the given expression is valid and only contains digits,
# '?', ':', 'T', and 'F' where 'T' is true and 'F' is false. All the numbers in the
# expression are one-digit numbers (i.e., in the range [0, 9]).

# The conditional expressions group right-to-left (as usual in most languages),
# the result of the expression will always evaluate to either a digit, 'T' or 'F'.


# Approach: Use stack to store the expression from the end, and whenever we see the query
# "?" as our most recent entry (NOT OUR CURRENT ENTRY), it means that the 4 recent entries
# including "?" will give us the ternary expression components - a "?", followed by a
# digit/bool(TRUE), followed by ":", and finally a digit/bool(FALSE). We then process the
# ternary operator (the current entry should tell us if we need to choose the TRUE digit/bool
# or FALSE one...


def parseTernary(expression):

    stack = []

    for s in expression:

        # If the last recent entry in stack was "?", that means our current
        # s should be a boolean T or F:
        if stack and stack[-1] == "?":

            # Remove "?"
            stack.pop()
            # Get the ternary expression's truth portion:
            t_portion = stack.pop()
            # Remove ":"
            stack.pop()
            # Get the ternary expression's false portion:
            f_portion = stack.pop()

            # Append t_portion or f_portion, depending on what our s is currently:
            if s == "T":
                stack.append(t_portion)
            else:
                stack.append(f_portion)

        # If we haven't reached a processable ternary expression, just keep appending
        # to the stack:
        else:
            stack.append(s)

    # Assuming the ternary expression was valid, there should only be one digit/bool left
    # in the stack. Return it:
    return stack[0]

