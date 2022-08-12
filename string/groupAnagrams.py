# My blind attempt at this problem:

def groupAnagrams(strs):

    result = []
    list_length = len(strs)

    while list_length > 0:

        sub_result = []
        current_word = strs.pop(0)
        sub_result.append(current_word)

        current_letters = {}

        for letter in current_word:

            if letter not in current_letters:
                current_letters[letter] = 1
            else:
                current_letters[letter] += 1

        for word in strs:
            check = current_letters.copy()

            for w in word:

                if w not in check:
                    break
                else:
                    check[w] -= 1

            # Write more here on determining whether to append string or not

        result.append(sub_result)


