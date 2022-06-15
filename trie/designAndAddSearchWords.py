# Basically same question as implement Trie, except
# with additional feature of being able to add wild
# card when searching for a word:

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    # addWord() is identical to insert() from Trie class:
    def addWord(self, word):

        current = self.root

        for letter in word:

            if letter not in current.children:
                current.children[letter] = TrieNode()

            current = current.children[letter]

        current.endOfWord = True

    # search() is similar to Trie's function w the same name,
    # except now we need to implement the ability to use dot
    # to match any letter:
    def search(self, word):

        def dfs_search(node, word_index):

            current = node

            for i in range(word_index, len(word)):
                letter = word[i]

                if letter == ".":
                    for entry in current.children:

                        if dfs_search(current.children[entry], i + 1):
                            return True

                    return False
                else:
                    if letter not in current.children:
                        return False
                    current = current.children[letter]

            return current.endOfWord

        # Execute the dfs_search from root:
        return dfs_search(self.root, 0)

