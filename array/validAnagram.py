# Easy problem where we use hash map to keep track of the number of
# occurrence of each character:

def validAnagram(s, t):

    # Edge case - if length of string does not match, they cannot be
    # valid anagrams of each other!
    if len(s) != len(t):
        return False

    # Initialize a dictionary to keep track of the letter count:
    count = {}

    # Loop through the length of the string. Both are same length
    # at this point since we checked using the if statement:
    for i in range(len(s)):
        # .get() method for dictionaries can take a second parameter,
        # which is a default value if certain key doesn't exist in the
        # dictionary:

        # Add 1 to the letter count for each letter in s
        # Subtract 1 from the letter count for each letter in t
        count[s[i]] = 1 + count.get(s[i], 0)
        count[t[i]] = count.get(t[i], 0) - 1

    # Now, loop through each key (letter) in the count dictionary, and
    # ensure that all counts are zero. If it's not zero, it means there's
    # a mismatch and the two strings are not anagrams of each other:
    for letter in count:
        if count[letter] != 0:
            return False

    # If the above for loop didn't return False, it means we have valid anagrams:
    return True


# Another Solution - sort two inputs individually and see if
# they match:
def validAnagramsSort(s, t):
    return sorted(s) == sorted(t)
