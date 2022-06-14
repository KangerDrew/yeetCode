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

