# Seemingly straight forward, but we must be careful to consider
# ALL the edge cases!

# When given a list of length 2 words, there are two types of words
# we can get from it:
# Category 1) A word where both letters are equal
# Category 2) A word with two different letters

# We'll handle how we store them depending on whether it belongs to
# category 1 or 2.

# For category 1 (same letters), we also need to keep track of any that
# may end up without any pairs. One of the leftover words can be used as
# a centerpiece, thus increasing the length of the palindrome.

# Finally, we use HashMap (NOT HashSet) to store the words. Since we're
# going to do linear scan, if we run into identical word more than once
# in a row. Using HashMap will allow us to keep track of same words, as
# we CANT do that with HashSet!!!
import collections


def longestPalindrome(words):

    # We use a special type of HashMap call collector! This makes it
    # easier to set up HashMap without weird logic & exceptions:
    stored = collections.Counter()

    # Set int variables to keep track of length of palindrome and the
    # number of unpaired words with same letters (as discussed earlier):
    unpaired = res = 0

    for w in words:

        # Are the letters identical?
        if w[0] == w[1]:
            # Check if we already have the word in HashSet. If we do,
            # remove it from the HashSet and increase the length of the
            # palindrome. Also take -1 from unpaired variable:
            if stored[w] > 0:
                unpaired -= 1
                stored[w] -= 1
                res += 4
            # Otherwise, we add it to the HashMap and mark down that there's
            # an unpaired word with identical letters:
            else:
                stored[w] += 1
                unpaired += 1
        # If the letters are not identical...
        else:
            # If the reverse of the word is in the HashMap, we increase
            # palindrome length, and remove the reverse from HashMap:
            if stored[w[::-1]] > 0:
                res += 4
                stored[w[::-1]] -= 1
            # Otherwise, add the word to the HashMap:
            else:
                stored[w] += 1

    # If there are any unpaired words with identical letters, one of those
    # can be used as a centerpiece of the palindrome:
    if unpaired > 0:
        res += 2

    # Return the final palindrome length:
    return res
