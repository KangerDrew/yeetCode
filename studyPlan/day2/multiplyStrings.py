# We are NOT allowed to cast the inputs into int() directly.
# However, we can convert individual digits into the int() temporarily.

def multiplyStrings(num1, num2):
    # Edge case - Simply return 0 if either of the input is zero:
    if num1 == "0" or num2 == "0":
        return "0"

    # We know that the maximum number of digits of the resulting value
    # would be no more than the combined number of digits from both
    # inputs. Thus, we'll use an array to keep track of each values:
    res = [0 for i in range(len(num1) + len(num2))]

    # For us to use "elementary math" to multiply the values, we need to
    # inverse the two string inputs so our indexes i1 and i2 can correctly
    # use the right values:
    num1, num2 = num1[::-1], num2[::-1]

    for i1 in range(len(num1)):
        for i2 in range(len(num2)):
            digit = int(num1[i1]) * int(num2[i2])

            # First, add the digit onto the index i1 + i2. This may cause an
            # overflow of digit that's length = 2, but keep as is for now.
            res[i1 + i2] += digit
            # Then, add the 1st digit (10 value) to the index ahead of i1 + i2.
            # This may ALSO cause an overflow, but it will be resolved on further
            # for loop iterations down the line.
            res[i1 + i2 + 1] += (res[i1 + i2] // 10)
            # We accounted for the overflow by adding the 1st digit to the next
            # index. We don't need it anymore so set the value at i1 + i2 to be
            # the 2nd index only:
            res[i1 + i2] = res[i1 + i2] % 10

    # Now, we just need to invert the res array back, and remove any extra
    # 0's at the beginning:
    res, beg = res[::-1], 0
    while beg < len(res) and res[beg] == 0:
        beg += 1

    # Convert the int values to str:
    res = [str(j) for j in res[beg:]]
    # Join the strings together and return it:
    return "".join(res)


print(multiplyStrings("999", "999"))
