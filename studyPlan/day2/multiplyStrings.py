# We are NOT allowed to cast the inputs into int() directly.
# However, we can convert individual digits into the int() temporarily.

def multiplyStrings(num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"

    res = [0 for i in range(len(num1) + len(num2))]
    num1, num2 = num1[::-1], num2[::-1]

    for i1 in range(len(num1)):
        for i2 in range(len(num2)):
            digit = int(num1[i1]) * int(num2[i2])

            res[i1 + i2] += digit
            res[i1 + i2 + 1] += (res[i1 + i2] // 10)
            res[i1 + i2] = res[i1 + i2] % 10

    res, beg = res[::-1], 0
    while beg < len(res) and res[beg] == 0:
        beg += 1

    res = [str(j) for j in res[beg:]]
    return "".join(res)
