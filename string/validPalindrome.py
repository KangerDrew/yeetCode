import re


def validPalindrome(s):

    def validString(x):
        return (ord("a") <= ord(x.lower()) <= ord("z")) or (
                ord("0") <= ord(x) <= ord("9"))

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


# print(validPalindrome("A man, a plan, a canal: Panama"))
print(validPalindrome(". ,"))


def superShort(s):
    # Use regex to remove any characters that do not match a-z, A-Z, or 0-9,
    # then lowercase them:
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    # s[::-1] returns a flipped s. If it's a valid palindrome, string should be same:
    return s == s[::-1]


print(superShort("A man, a plan, a canal: Panama"))
