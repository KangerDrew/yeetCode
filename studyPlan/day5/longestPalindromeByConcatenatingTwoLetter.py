import collections

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

# O(n) time complexity, with O(n) memory:

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


# Found a really cool approach that uses grid instead of HashMap to store
# the letters:

# Slightly less memory efficient (O(26*26)), but similar runtime O(n).

# ***Ideally use the first solution, as it is faster and easier to understand!***
def longestPalindromeGrid(words):

    # Create a 26 x 26 grid, where row represents first letter,
    # and column represents the second letter of the word:
    letter_count = [[0 for _ in range(26)] for _ in range(26)]
    res = 0

    for w in words:

        # Use ascii comparison to get the index value of the letter:
        l1, l2 = ord(w[0]) - ord('a'), ord(w[1]) - ord('a')

        # Check if the reverse of the word is in the grid. If so, add
        # 4 to the palindrome length and remove the reverse:
        if letter_count[l2][l1] > 0:
            res += 4
            letter_count[l2][l1] -= 1
        # If not, add the word to the grid:
        else:
            letter_count[l1][l2] += 1

    # Now, loop through the grid to see if there are any words with
    # identical letters remained unused:
    for i in range(26):

        # If yes, we add 2 to the palindrome length as it can be used
        # as a center of the palindrome. Remember to break after!
        if letter_count[i][i] > 0:
            res += 2
            break

    # Return the palindrome length result:
    return res
