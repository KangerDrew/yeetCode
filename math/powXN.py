# The most logical solution is to simply multiply the input by the
# specified amount, and return it... However we need much faster
# solution than this!

def powSlow(x, n):

    sol = 1

    while n > 0:
        sol *= x
        n -= 1

    return sol


print(powSlow(3,2))
