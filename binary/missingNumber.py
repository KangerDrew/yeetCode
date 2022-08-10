# Besides the brute-force method (involves sorting the input array and checking
# which one is missing - O(n log n)), linear time solution can be achieved
# by using hashset to store all the values from the input, looping through
# the range to see which numbers are available. However, this also requires
# constant space memory for the hashset. There are two solutions that can
# solve this problem using constant space AND linear time.

# Solution 1: Bit Manipulation

# When we perform XOR bit operation on two identical numbers, we get zero:
# Ex 1:   1 0 0 0 1 0
#         1 0 0 0 1 0
#       --------------
#     ==> 0 0 0 0 0 0

# The same result is achieved when we have several pairs of identical numbers, even
# if the orders are mixed up:
# Ex 2:   1 0 0 0 1 0    (34)
#         0 1 0 0 0 1    (17)
#       --------------
#     ==> 1 1 0 0 1 1    (51)
#         0 1 0 0 0 1    (17)
#       --------------
#     ==> 1 0 0 0 1 0    (34) *Note how after we performed XOR on 17 again, we got back 34!*
#         1 0 0 0 1 0    (34)
#       --------------
#     ==> 0 0 0 0 0 0

# Thus, when we perform XOR bitwise operation on all the numbers in the input array, and all
# the values expected in the range, whatever is leftover will be the number that didn't have
# the corresponding pair from all the values in the range (i.e. missing number)!


def missingNumberBitwise(nums):
    val = len(nums)

    for n in nums:
        val ^= n

    for i in range(len(nums)):
        val ^= i

    return val


# Shorter way to write the above solution, using Python's enumerate function:
def missingNumberBitwiseShorter(nums):
    val = len(nums)

    for i, num in enumerate(nums):
        val ^= i ^ num

    return val


# Solution 2: Gauss Sum Formula - Actual Sum
