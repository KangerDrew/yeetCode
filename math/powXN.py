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


# print(powSlow(3, 2))

# The above solution will run at O(n) time complexity. We can improve
# this to O(log(n)), by cutting our workload in half. To do this, we
# use a divide and conquer method. This can be achieved by recognizing
# that when we calculate x ^ (n / 2), we don't need to run the algorithm
# for another n / 2 times, but instead just multiply x ^ (n / 2) twice
# to get the desired x ^ n:

def pow(x, n):

    def helper(x_h, n_h):
        # Base case 1: If x = 0, return 0
        if x_h == 0:
            return 0
        # Base case 2: If n = 0, we return 1 since x ^ 0 is always 1:
        if n_h == 0:
            return 1

        # Divide the work by half. If n is odd number, it'll be accounted
        # for in the return statement:
        val = helper(x_h, n_h // 2)
        # Multiply val by itself:
        val = val * val

        # Return val. But if the input n value was odd value,
        # we need to multiply the final work by x_h to account
        # for rounding down:
        return val if n_h % 2 == 0 else val * x_h

    # Input values into helper function, but use positive (abs) n value:
    res = helper(x, abs(n))
    # return solution, but return the inverse if the n was negative:
    return res if n > 0 else 1 / res


print(pow(2, 10))
