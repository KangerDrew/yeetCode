# We COULD use dynamic programming approach to solve this problem... but there is a
# easier way...

# We can loop through the string once, and at a select index, expand outwards using
# two pointers to check that a palindrome can be constructed, using that index as a
# center.

# If the two index starts at the same center point, we will get the longest ODD number
# length palindrome. If two index starts 1 index apart from each other, we will get the
# longest EVEN number length palindrome!


def longestPalindromeCenter(s):

    max_pal = ""
    str_len = 0

    for i in range(len(s)):

        # Odd length palindrome check:
        left, right = i, i

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        if (right - left) + 1 > str_len:
            # Remember, the right boundary is non-inclusive so we
            # need to get string from left, to "right + 1"
            max_pal = s[left:(right + 1)]

