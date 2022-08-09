# For this bit manipulation problem, we can break it down to 3 bit-shifting operators:

# XOR Operator - True when only one of them is true, which is also when they're
# not equal (used for simulating addition)

# & Operator - Only true when both quantities are true (used for carrying over extra 1)

# Leftshift Operator - Shifting a binary digit to the left (used in conjunction w & operator for
# calculating a carrying over value)

# Step 1: Use XOR Operator on two values, which will yield a binary value
# Step 2: Use & AND Leftshift operator on two values, which will give us a carrying over value to be added
# Step 3: Repeat step 1 and 2 with the values from each step until step 2 returns zero value.

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
print(3 << 1)
print(3 ^ 2)

