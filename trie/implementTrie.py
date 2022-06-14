# Trie (pronounced "try") is a tree data structure used to efficiently
# store and retrieve keys in dataset of strings.

# Trie has three functions: insert, search, and startsWith.
# insert adds a new string into the trie, and search returns a boolean
# depending on whether a string exists within a trie or not.

# While the first two functions are also available using HashSet (in O(1) time),
# it's the third function - startsWith, that makes trie data structure more
# versatile than HashSet.

# Third function, startsWith returns boolean based on whether there is a previously
# inserted string that has the input as prefix. In other words, if a word "apple"
# exists within the trie, startsWith("app") will return True!

# Popular use of trie: autocomplete, spellchecker

# We first need a TrieNode class, which will serve as nodes for our
# trie data structure's nodes:
class TrieNode:
    def __init__(self):
        # Instantiating trie node should give us a attribute called
        # children, which is initialized as an empty dictionary.

        # Unlike binary tree (where we have left and right children),
        # we need to account for 26 (for english) possible children nodes,
        # and the easiest way to do that without creating 26 separate
        # attributes is to create a dictionary, where the key is the
        # alphabet character, and value will be a TrieNode with its own
        # branching children and endOfWord boolean:
        self.children = {}

        # the endOfWord attribute is to mark the current node as
        # an endOfWord. When search function is called, we can check
        # this attribute to confirm that a certain specific word was
        # indeed entered (see search function for more detail)
        self.endOfWord = False


# Below is the implementation of Trie data structure:
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root

        for character in word:
            if character not in current.children:
                current.children[character] = TrieNode()

            current = current.children[character]

        current.endOfWord = True

    def search(self, word):

        current = self.root

        for character in word:
            if character not in current.children:
                return False

            current = current.children[character]

        return current.endOfWord

    def startsWith(self, prefix):
        current = self.root

        for character in prefix:
            if character not in current.children:
                return False

            current = current.children[character]

        return True


