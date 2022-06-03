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


# sliding window technique:
def noRepeatingChar(s):

    contained_char = set()
    left = 0
    max_len = 0

    for right in range(len(s)):

        while s[right] in contained_char:
            contained_char.remove(s[left])
            left += 1

        contained_char.add(s[right])
        max_len = max(max_len, right + 1 - left)

    return max_len

