from collections import deque
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
        # starting_word_index
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

    # Iterative version of search function:
    def search_itr(self, word):

        # Initialize stack structure using deque (noticeably faster
        # than using regular python list). We add a tuple that consists
        # of following - root TrieNode, and the index value (starting at
        # 0 from the root):
        stack = deque([(self.root, 0)])

        while stack:

            # Pop from stack:
            current, index = stack.pop()

            # This if statement will check if we've reached the end
            # of the word. If the index is equal to the length of the
            # word, it means we've successfully traversed down the trie
            # and just need to check current.endOfWord:
            if index == len(word):
                if current.endOfWord:
                    return True
                else:
                    # This continue statement is necessary, as this will
                    # skip the current loop and prevent code below from
                    # crashing due to IndexError.
                    continue

            # Get the letter we're checking from the input:
            letter = word[index]

            # Check if we're provided a wild card option - "."
            if letter == ".":

                # We need to loop through options available in current.children:
                for entry in current.children:
                    # Although the if statement below is unnecessary (first if statement
                    # should catch edge cases), this is just to ensure we do not over-index:
                    if index < len(word):
                        # Append the TrieNode to stack, along with the incremented index value:
                        stack.append((current.children[entry], index + 1))

            # For any other string, we only need to check if the letter is
            # part of the children:
            else:

                # If letter is not part of the entry (not in children),
                # it means that the word doesn't exist in this particular
                # Trie path. However, the word could exist elsewhere so we
                # do not return False, but instead use continue statement
                # to skip the rest of the loop and move onto the next node
                # in the stack:
                if letter not in current.children:
                    continue

                # Again, unnecessary if statement but we'll add it in so we
                # do not over-index:
                if index < len(word):
                    # Append TrieNode, and the incremented index value:
                    stack.append((current.children[letter], index + 1))

        # If we exit the while loop without returning True, it
        # means the word was not found:
        return False


newTrie = WordDictionary()
newTrie.addWord("bad")
newTrie.addWord("dad")
newTrie.addWord("mad")
print(newTrie.search_itr("pad"))  # Should be False
print(newTrie.search_itr("bad"))  # Should be True
print(newTrie.search(".ad"))  # Should be True
print(newTrie.search("b..fa"))  # Should be True
