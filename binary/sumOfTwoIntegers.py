# For this bit manipulation problem, we can break it down to 3 bit-shifting operators:

# & Operator - Only true when both quantities are true (used for carrying over extra 1)

# XOR Operator - True when only one of them is true, which is also when they're
# not equal (used for simulating addition)

# Leftshift Operator - Shifting

def getSumPython(a, b):

    mask = 0xffffffff

    while b != 0:
        tmp = (a & b) << 1
        a = (a ^ b) & mask
        b = tmp & mask

    if a > mask // 2:
        return ~(a ^ mask)
    else:
        return a


print(getSumPython(2, 3))

