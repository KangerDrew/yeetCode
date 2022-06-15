# Basically same question as implement Trie, except
# with additional feature of being able to add wild
# card when searching for a word:

class WordNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary:
    def __init__(self):
        self.root = WordNode()

    # addWord() is identical to insert() from Trie class:
    def addWord(self, word):

        current = self.root

        for letter in word:

            if letter not in current.children:
                current.children[letter] = WordNode()

            current = current.children[letter]

        current.endOfWord = True

    # search() is similar to Trie's function w the same name,
    # except now we need to implement the ability to use dot
    # to match any letter:
    def search(self, word):
        current = self.root

