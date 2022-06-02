def trashNoRepeatingChar(s):
    n = len(s)

    if n == 1:
        return 1

    res = 0
    for i in range(n):

        # New set at the beginning of each outer loop:
        check_set = set()
        temp_max = 0

        for j in range(i, n):

            if s[j] in check_set:
                res = max(temp_max, res)
                break

            temp_max += 1
            check_set.add(s[j])

            if j == n - 1:
                res = max(temp_max, res)

    return res


print(trashNoRepeatingChar("au"))
