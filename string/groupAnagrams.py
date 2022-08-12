# My blind attempt at this problem:

def groupAnagramsRAW(strs):

    result = []

    while len(strs) > 0:

        sub_result = []
        current_word = strs.pop(0)
        sub_result.append(current_word)

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

#
# test_string = "tester"
# for i, letter in enumerate(test_string):
#     if letter == "b":
#         break
#
# if i < len(test_string) - 1:
#     print("broken early")


print(groupAnagramsRAW(["eat","tea","tan","ate","nat","bat"]))
