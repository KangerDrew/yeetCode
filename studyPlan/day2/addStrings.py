# This was not assigned for today, but I wanted to see if I can
# use the same logic from Multiply String:

def addStrings(num1, num2):

    if num1 == "0" and num2 == "0":
        return "0"

    res_length = max(len(num1), len(num2)) + 1
    res = [0 for v in range(res_length)]

    num1, num2 = num1[::-1], num2[::-1]

    for i in range(res_length - 1):
        val1 = int(num1[i]) if i < len(num1) else 0
        val2 = int(num2[i]) if i < len(num2) else 0
        digit = val1 + val2

        res[i] += digit
        res[i + 1] += res[i] // 10
        res[i] = res[i] % 10

    res, beg = res[::-1], 0

    print(res)

    while beg < len(res) and res[beg] == 0:
        beg += 1

    res = [str(j) for j in res]
    return "".join(res[beg:])
