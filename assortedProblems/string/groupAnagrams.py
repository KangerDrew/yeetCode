from collections import defaultdict


# My blind attempt at this problem:
def groupAnagramsBLIND(strs):
    result = []

    while len(strs) > 0:

        sub_result = []
        current_word = strs.pop(0)
        sub_result.append(current_word)

        if len(current_word) == 0:

            ind = 0
            while len(strs) > ind:

                if len(strs[ind]) == 0:
                    sub_result.append(strs.pop(ind))
                else:
                    ind += 1

            result.append(sub_result)
            continue

        current_letters = {}

        for letter in current_word:

            if letter not in current_letters:
                current_letters[letter] = 1
            else:
                current_letters[letter] += 1

        for i, word in enumerate(strs):
            check = current_letters.copy()

            for j, w in enumerate(word):

                if w not in check:
                    break
                elif check[w] <= 0:
                    break
                else:
                    check[w] -= 1

            if j < len(word) - 1:
                continue
            else:
                new_sub_word = strs.pop(i)
                sub_result.append(new_sub_word)

        result.append(sub_result)

    return result


# test_string = "tester"
# for i, letter in enumerate(test_string):
#     if letter == "b":
#         break
#
# if i < len(test_string) - 1:
#     print("broken early")


# print(groupAnagramsBLIND(["eat", "tea", "tan", "ate", "nat", "bat"]))
# print(groupAnagramsBLIND(["", "b"]))
print(groupAnagramsBLIND(["", "", ""]))
print(groupAnagramsBLIND(["h", "h", "h"]))


# The correct solution - convert each letter to a list of length 26, where
# each index is a number of letters in the word. Then, convert those list to
# tuples so they can be used as a key to a dictionary, where the default value
# be a list that we can append our string to.

def groupAnagrams(strs):

    # Below is a dictionary, where keys will be a tuples that
    # indicate how many letters were in
    matched_strings = defaultdict(list)

    for s in strs:
        count = [0] * 26  # there are 26 letters in english

        for c in s:
            # use ord() function to get the unicode value of the letter
            # subtracted by that of "a":
            count[ord(c) - ord("a")] += 1

        # For example, if our letter was "abc", then the resulting list we get
        # would be [1, 1, 1, 0, 0, 0, 0... ALL ZEROS..., 0, 0]

        # We need to use the list as a key in our dictionary, but because list is mutable
        # we can't do that. Instead, we must convert it to tuple for it to be used as a key:
        matched_strings[tuple(count)].append(s)

    # Return the values (should be bunch of lists) of the matched_strings dictionary:
    return matched_strings.values()


