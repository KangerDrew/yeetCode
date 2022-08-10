# We need to return an array (list), where each index contains
# a number of 1's in the binary representation of the index.



def countingBits(n):

    returning_list = [0]
    power_two_tracker = 1

    for i in range(n + 1):

        if i == power_two_tracker * 2:
            power_two_tracker *= 2