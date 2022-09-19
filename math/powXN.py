# The most logical solution is to simply multiply the input by the
# specified amount, and return it... However we need much faster
# solution than this!

def powSlow(x, n):

    sol = 1
    power = abs(n)

    while power > 0:
        sol *= x
        power -= 1

    return sol if n > 0 else 1 / sol


print(powSlow(3, 2))
