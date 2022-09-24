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

# Instead of testing out every possible substring, we use two pointers,
# and incrementing the right O(n) times. We can use a set to keep track
# of which letter has been traversed. If we do run across the letter
# we've seen before, we remove the letter and increment the left pointer
# till our set is filled with unique letters:

def noRepeatingChar(s):

    # Initialize set to keep track of letters:
    contained_char = set()
    left = 0
    max_len = 0

    # Increment right pointer:
    for right in range(len(s)):

        # If the letter at the right pointer is in the
        # contained_char, we increment the left pointer
        # until we only have unique letters:
        while s[right] in contained_char:
            contained_char.remove(s[left])
            left += 1

        # Add the letter at the right pointer to the set:
        contained_char.add(s[right])
        # Calculate the max length. Important that we do this
        # at each iteration as we can't guarantee that the final
        # positions of the pointers give us the max length. It
        # could occur in the middle of the iteration:
        max_len = max(max_len, right + 1 - left)

    return max_len


# We can optimize the process above using hashmap (dictionary)
# instead of hashset. Use dictionary to store the index of the
# letter, and instead of using while loop to increment the left
# pointer, we can immediately jump to the correct position:

def noRepeatingCharOpt(s):

    max_len = 0
    # use dictionary instead of set:
    contained_char = {}
    left = 0

    for right in range(len(s)):

        if s[right] in contained_char:
            left = max(contained_char[right] + 1, left)

        contained_char[s[right]] = right
        max_len = max(max_len, right + 1 - left)

    return max_len
