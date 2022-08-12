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
print(groupAnagramsBLIND(["h","h","h"]))
