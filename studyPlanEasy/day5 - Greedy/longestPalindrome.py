import collections

# My first attempt:
def longestPalindrome(s):

    odd_num_letter = False
    palindrome_len = 0
    letter_count = collections.defaultdict(int)

    for letter in s:
        letter_count[letter] += 1

    for letter in letter_count:

        if not odd_num_letter and letter_count[letter] % 2 == 1:
            odd_num_letter = True

        palindrome_len += letter_count[letter] // 2 * 2

    if odd_num_letter:
        palindrome_len += 1

    return palindrome_len


# Slight optimization, to remove odd_num_letter boolean. Originally this variable
# was used to keep track of whether we managed to find a unique letter (if the count
# of that letter is odd) that could be used as the center of palindrome. However,
# we can instead just check the length of the palindrome that we're keeping!

# If we first encounter a letter with odd number count, we check if our palindrome length
# is odd or even. If it's odd, it means that we've already added a unique center. Otherwise,
# if that is a first time we've encountered an odd number count letter, we increment the
# palindrome count by 1!

def longestPalindromeBetter(s):
    palindrome_len = 0
    # letter_count = collections.defaultdict(int)
    #
    # for letter in s:
    #     letter_count[letter] += 1

    # Better way to do letter_count:
    letter_count = collections.Counter(s)

    for letter in letter_count:

        if palindrome_len % 2 == 0 and letter_count[letter] % 2 == 1:
            palindrome_len += 1

        palindrome_len += letter_count[letter] // 2 * 2

    return palindrome_len
