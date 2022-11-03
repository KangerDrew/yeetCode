# First attempt:

def fibonacci(n):

    if n == 0:
        return 0
    if n < 3:
        return 1

    # fib_arr = [1, 1]
    #
    # while len(fib_arr) < n:
    #     fib_arr.append(fib_arr[-1] + fib_arr[-2])
    #
    # return fib_arr[-1]

    prev, current = 1, 1
    n -= 2

    while n > 0:
        prev, current = current, prev + current
        n -= 1

    return current
