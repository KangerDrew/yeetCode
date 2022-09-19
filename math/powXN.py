# The most logical solution is to simply multiply the input by the
# specified amount, and return it... However we need much faster
# solution than this!

def powSlow(x, n):

    # Initialize a variable we'll use to return the answer
    sol = 1
    # Get the absolute (positive) value of n:
    power = abs(n)

    # Loop until we finished multiplying by abs(n) times
    while power > 0:
        sol *= x
        power -= 1

    # If n was positive, return sol. If not, return the inverse:
    return sol if n > 0 else 1 / sol


print(powSlow(3, 2))
