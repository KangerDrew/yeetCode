def validPalindrome(s):

    def validString(x):
        return (ord("a") <= ord(x.lower()) and ord(x.lower()) <= ord("z")) or (
                    ord("0") <= ord(x) and ord(x) <= ord("9"))

    left, right = 0, len(s) - 1

    while left < right:

        while left < right and not validString(s[left]):
            left += 1
        while left < right and not validString(s[right]):
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


print(validPalindrome("A man, a plan, a canal: Panama"))
