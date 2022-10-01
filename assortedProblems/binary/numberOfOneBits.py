some_string = "011101"
some_val = 8
# print(some_string >> 1)
print(some_val >> 2)


# First solution uses modulo function, where we check if modulo 2 of input is non-zero.
# If it is, we add 1 to the counter. Then, we right shift our input and see if modulo of
# that is non-zero. We continue to do this until the shifted input value is zero:

# Ex:   100101 ==> +1
#        10010 ==> N/A
#         1001 ==> +1
#          100 ==> N/A
#           10 ==> N/A
#            1 ==> +1
# Solution: 3

def numOfOneBits(n):

    counter = 0

    while n != 0:
        # Check if rightmost bit value is 1
        if n % 2 != 0:
            counter += 1

        # Rightshift
        n = n >> 1

    return counter


# Alternate solution involves using & bitwise operation. When we perform
# bitwise & operation on input and input - 1, it returns a new bit value
# where leftmost 1 value becomes zero (see solution for visual guide)
def numOfOneBitsAnd(n):

    counter = 0

    while n != 0:

        n = n & (n - 1)
        counter += 1

    return counter

