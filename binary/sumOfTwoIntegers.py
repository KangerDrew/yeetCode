# For this bit manipulation problem, there are three





def getSumPython(a, b):

    mask = 0xffffffff

    print(mask)

    while b != 0:
        tmp = (a & b) << 1
        a = (a ^ b) & mask
        b = tmp & mask

    if a > mask // 2:
        return ~(a ^ mask)
    else:
        return a


print(getSum(2, 3))

