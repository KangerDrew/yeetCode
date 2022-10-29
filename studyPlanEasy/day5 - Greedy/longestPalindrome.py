# My first attempt:
import collections


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
