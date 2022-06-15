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

        # The dfs function below takes TrieNode, and the
        #
        def dfs_search_recursive(node, starting_word_index):

            # Take the input node as current:
            current = node

            # Loop through each index of the word, starting from
            # the starting_word_index:
            for i in range(starting_word_index, len(word)):

                letter = word[i]
                # If the letter we're looping through is ".", it means we
                # have to check every single entries made on this level from
                # current node:
                if letter == ".":
                    # Loop through every entry from current node's children:
                    for entry in current.children:
                        # Recursively execute dfs_search_recursive, using
                        # current.children[entry] TrieNode. Also use i + 1
                        # as starting_word index, to correctly loop from the
                        # proper starting position:
                        if dfs_search_recursive(current.children[entry], i + 1):
                            return True
                    # if above didn't return True, it means no search was returned:
                    return False
                else:
                    # Below is the exact same search function as that from
                    # implementTrie problem:
                    if letter not in current.children:
                        return False
                    current = current.children[letter]

            return current.endOfWord

        # Execute the search from root using helper function:
        return dfs_search_recursive(self.root, 0)

