import collections
# New two pointer problem. We initialize a dictionary that keeps track of the letters
# in each substring. We will increment the left and right pointers on the main string s,
# removing and adding the letters using those pointers and checking to see if the
# current substring is an anagram of the input p:


def findAnagrams(s, p):
    # If the length of s is shorter than p, then it's impossible for
    # s to contain any anagram of p in the first place:
    if len(p) > len(s):
        return []

    # Define a dictionary that contains the number of letters in the p.
    # We can simply use Counter to do this:
    p_dict = collections.Counter(p)

