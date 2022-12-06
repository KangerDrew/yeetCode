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
