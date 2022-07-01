def wordBreak(s, wordDict):

    word_length = len(s)
    # tabulation list
    valid_check = [False for i in range(word_length + 1)]
    valid_check[0] = True

    for letter in range(1, word_length + 1):

        for checkingWord in wordDict:

            if valid_check[letter - 1] is True and s[(letter - 1):(letter - 1 + len(checkingWord))] == checkingWord:
                valid_check[letter - 1 + len(checkingWord)] = True

    return valid_check[-1]


print(wordBreak("leetcode", ["leet", "code"]))
print(wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
