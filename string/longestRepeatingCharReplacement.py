def charReplacementFast(s, k):

    # Dictionary (hash map) of the count of each letters in the string s:
    letters = {}

    # Index for left pointer:
    left = 0
    # Below is a variable that indicates the count of the most
    # common letter within a specified sub-string.
    most_common_letter_count = 0

    # This is a value we'll return once we exit the for loop below:
    longest_sub = 0

    # Loop through, where "right" is the index for the right pointer
    # that gets incremented every loop:
    for right in range(len(s)):

        # if s[right] not in letters:
        #     letters[s[right]] = 1
        # else:
        #     letters[s[right]] += 1

        # Better than if else statement above. .get() method doesn't throw
        # error if value doesn't exist in dictionary doesn't contain the
        # value. The value defaults to 0 if it doesn't exist in the dictionary.
        letters[s[right]] = 1 + letters.get(s[right], 0)

        # Most common letter count might change, if the newly added letter
        # makes that current letter the greatest recurring letter in the substring

        # For example, in the string "ABB" on the third iteration of the for loop,
        # B will become the new "most_common_letter". Therefore, we must replace
        # it using python's max() function as shown below.
        # letters[s[right]] returns the count of character at index "right" in the
        # current substring!
        most_common_letter_count = max(most_common_letter_count, letters[s[right]])

        # We take the length of the substring (right + 1 - left), and subtract it by
        # the most_common_letter_count. This will give us the number of remaining
        # characters in the substring.

        # If k value is greater than this, that means the current substring is valid
        # since we will be able to replace any characters that needs replacement.

        # Otherwise (while loop condition below), it means that we can't increment
        # the right index since larger substring will not be valid. Instead, we move
        # the left index one by one until we are able to produce a "longest substring
        # that is valid after replacing k characters":
        while (right + 1 - left - most_common_letter_count) > k:
            letters[s[left]] -= 1
            left += 1

        # We take the largest between the current substring length (right + 1 - left) and
        # the existing longest_sub:
        longest_sub = max(right + 1 - left, longest_sub)

    return longest_sub

