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

        # It is important to remember that each individual TrieNode
        # does NOT have an attribute called "value". Instead, we have
        # children dictionary that "points to the direction of next letter
        # if it exists within the trie". DO NOT CONFUSE THIS WITH THE WAY
        # BINARY TREE WORKS!

        # Also unlike binary tree (where we have left and right children),
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
        # When trie is initialized, we start with a root, which should
        # be a TrieNode with empty children dictionary. As we insert
        # words, the root TrieNode's children dictionary will get more
        # entries that point to different letters:
        self.root = TrieNode()

    def insert(self, word):
        # We need to traverse down the Trie, and insert
        # new TrieNodes as necessary. Start from the root:
        current = self.root

        # Loop through each letter in word input:
        for letter in word:
            # If the character doesn't exist in the current TrieNode's
            # children, we instantiate a new TrieNode as a value using
            # letter as the key:
            if letter not in current.children:
                current.children[letter] = TrieNode()

            # Step into the letter (traverse down the Trie), by updating
            # the current pointer:
            current = current.children[letter]

        # Once we finish traversing down the Trie to the final letter's position,
        # we set the endOfWord attribute for that TrieNode as True, indicating
        # that a specific entry has finished on this TrieNode:
        current.endOfWord = True

    def search(self, word):

        # Same as insert function, we traverse down Trie from root:
        current = self.root

        # Loop through each letter in word input:
        for letter in word:

            # For search function, if a letter is not present in the
            # current TrieNode's children, it means no such entry exists,
            # so return False:
            if letter not in current.children:
                return False

            # Otherwise, we continue to traverse down the Trie:
            current = current.children[letter]

        # If the final TrieNode was marked as end of word, that means the
        # word input does exist in Trie. If not, it means that specific word
        # was never inserted. Here we simply return current.endOfWord:
        return current.endOfWord

    def startsWith(self, prefix):
        # This function is pretty much identical to search() function,
        # except for the final return statement
        current = self.root

        for letter in prefix:
            if letter not in current.children:
                return False

            current = current.children[letter]

        # If we successfully traversed down the Trie up till this point, it
        # means that there are entry(ies) that does start with the provided
        # prefix. Thus, we simply return True:
        return True
